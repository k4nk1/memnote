<script setup>
import { ref } from 'vue';
import { useAPI } from '../composables/useAPI';
import { useRouter } from 'vue-router';

const router = useRouter();
const APIs = useAPI();

const nid = router.currentRoute.value.params.nid;
const switchVisibility = (e) => {
    e.target.style.color = e.target.style.color !== 'rgb(255, 0, 0)' ? 'rgba(255, 0, 0)' : 'rgba(255, 0, 0, 0)';
};
const loadNote = async () => {
    const note = await APIs.getNote(nid);
    document.getElementsByClassName('title')[0].textContent = note.title;
    var content = note.content;
    content = content.replace(/<blank>/g, '<button class="blank">');
    content = content.replace(/<\/blank>/g, '</button>');
    document.getElementsByClassName('content')[0].innerHTML = content;
    var blanks = document.getElementsByClassName('blank')
    Array.from(blanks).forEach((e) => e.onclick = switchVisibility);
}
(async () => await loadNote())();
</script>

<template>
    <div class="container">
        <div class="title">
            <h1>{{ title }}</h1>
        </div>
        <div class="content">
            {{ content }}
        </div>
    </div>
</template>

<style>
.content{
    text-align: left;
}
.blank{
    border: 1px dashed #aaa;
    border-radius: 10px;
    padding: 3px;
    color: rgba(0, 0, 0, 0);
}

</style>