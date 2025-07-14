<script setup>
import { ref } from 'vue';
import { useUID } from '../composables/useUID';
import { useAPI } from '../composables/useAPI';
import { useRouter } from 'vue-router';

import { QuillEditor, Quill } from '@vueup/vue-quill';
import '@vueup/vue-quill/dist/vue-quill.snow.css';
import MarkdownShortcuts from 'quill-markdown-shortcuts';

const editor = ref(null);
let quill = null;
const Inline = Quill.import('blots/inline');
class Blank extends Inline{
    static blotName = 'blank';
    static tagName = 'blank';
};
Quill.register('formats/blank', Blank);
const onReady = () => {
    quill = editor.value.getQuill();
    document.getElementsByClassName('ql-blank')[0].innerHTML = "<svg viewBox=\"0 0 24 24\"><path d=\"M15,5H17V3H15M15,21H17V19H15M11,5H13V3H11M19,5H21V3H19M19,9H21V7H19M19,21H21V19H19M19,13H21V11H19M19,17H21V15H19M3,5H5V3H3M3,9H5V7H3M3,13H5V11H3M3,17H5V15H3M3,21H5V19H3M11,21H13V19H11M7,21H9V19H7M7,5H9V3H7V5Z\" /></svg>";
};
const createBlank = () => {
    quill.format('blank', true);
};

const router = useRouter();
const APIs = useAPI(await useUID());

const nid = router.currentRoute.value.params.nid;

const title = ref('');
const content = ref('');
let timer = 0;
const saving = ref(false);

const toolbar = [
    'bold', 'underline', {'header': 1}, {'header': 2}, {'color': []}, {'list': 'bullet'}, 'blank'
]

const modules = [{
    name: 'markdownShortcuts',  
    module: MarkdownShortcuts,
    options: {}
}];

const loadNote = async () => {
    const note = await APIs.getNote(nid);
    title.value = note.title;
    content.value = note.content;
}

const saveNote = () => {
    APIs.editNote(nid, title.value, content.value);
    saving.value = false;
};
const onChange = () => {
    if(timer) clearTimeout(timer);
    timer = setTimeout(saveNote, 3000);
    saving.value = true;
};
(async () => await loadNote())();
</script>

<template>
    <div class="container">
        <div class="sub-container">
            <input type="text" id="title-input" v-model="title" @change="onChange">
        </div>
        <div class="sub-container">
            <v-btn class="action" variant="text" prepend-icon="mdi-content-save-outline" @click="saveNote" v-if="!saving">保存</v-btn>
            <vue-loading type="spin" color="#aaa"></vue-loading>
            <v-btn class="action" variant="text" prepend-icon="mdi-checkbox-multiple-marked-outline">回答</v-btn>
            <v-btn class="action" variant="text" prepend-icon="mdi-share-variant-outline">回答URLをコピー</v-btn>
            <v-btn class="action" variant="text" prepend-icon="mdi-delete-outline">削除</v-btn>
        </div>
        <QuillEditor ref="editor" :toolbar="toolbar" theme="snow" contentType="html" v-model:content="content" @update:content="onChange" @ready="onReady" placeholder="ここにテキストを入力..." :modules="modules" />
    </div>
</template>

<style scoped>
.container{
    padding-top: 10px;
    width: 1000px;
    max-width: 100%;
    margin: auto;
    box-shadow: 0 0 25px 0 #ccc;
}
.sub-container{
    padding-left: 1%;
    border-left: 1px solid #d1d5db;
    border-right: 1px solid #d1d5db;
    text-align: left;
}
#title-input{
    font-size: 24px;
    width: 99%;
}

.action{
    margin: 5px 2px;
    padding: 0px 5px !important;
    font-size: 16px;
    font-weight: bolder;
}
.loader {
  font-size: 10px;
  margin: 50px auto;
  text-indent: -9999em;
  width: 11em;
  height: 11em;
  border-radius: 50%;
  background: #ffffff;
  background: -moz-linear-gradient(left, #ffffff 10%, rgba(255, 255, 255, 0) 42%);
  background: -webkit-linear-gradient(left, #ffffff 10%, rgba(255, 255, 255, 0) 42%);
  background: -o-linear-gradient(left, #ffffff 10%, rgba(255, 255, 255, 0) 42%);
  background: -ms-linear-gradient(left, #ffffff 10%, rgba(255, 255, 255, 0) 42%);
  background: linear-gradient(to right, #ffffff 10%, rgba(255, 255, 255, 0) 42%);
  position: relative;
  -webkit-animation: load3 1.4s infinite linear;
  animation: load3 1.4s infinite linear;
  -webkit-transform: translateZ(0);
  -ms-transform: translateZ(0);
  transform: translateZ(0);
}
.loader:before {
  width: 50%;
  height: 50%;
  background: #ffffff;
  border-radius: 100% 0 0 0;
  position: absolute;
  top: 0;
  left: 0;
  content: '';
}
.loader:after {
  background: #000000;
  width: 75%;
  height: 75%;
  border-radius: 50%;
  content: '';
  margin: auto;
  position: absolute;
  top: 0;
  left: 0;
  bottom: 0;
  right: 0;
}
@-webkit-keyframes load3 {
  0% {
    -webkit-transform: rotate(0deg);
    transform: rotate(0deg);
  }
  100% {
    -webkit-transform: rotate(360deg);
    transform: rotate(360deg);
  }
}
@keyframes load3 {
  0% {
    -webkit-transform: rotate(0deg);
    transform: rotate(0deg);
  }
  100% {
    -webkit-transform: rotate(360deg);
    transform: rotate(360deg);
  }
}

</style>

<style>
.ql-editor blank{
    border: 1px dashed #aaa;
    border-radius: 10px;
    padding: 3px;
    background-color: #ddd;
}
.ql-editor{
    min-height: 100vh;
    font-size: 20px;   
}
</style>