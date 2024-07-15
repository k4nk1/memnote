<script setup>
    import { ref } from 'vue'
    import { useAPI } from '../composables/useAPI';
    import { useUID } from '../composables/useUID';
    
    const APIs = useAPI(await useUID());

    const loading = ref(true);
    const notes = ref([]);
    const rename_dialog = ref(false);
    const delete_dialog = ref(false);
    const target_id = ref('');
    const title = ref('');

    const loadNotes = async () => {
        loading.value = true;
        notes.value = await APIs.getMyNotes();
        loading.value = false;
    }

    const openRenameDialog = (note) => {
        rename_dialog.value = true;
        target_id.value = note.id;
        title.value = note.title;
    }
    const openDeleteDialog = (note) => {
        delete_dialog.value = true;
        target_id.value = note.id;
        title.value = note.title;
    }
    const renameNote = async (nid) => {
        await APIs.renameNote(nid, title.value);
        rename_dialog.value = false;
        setTimeout(loadNotes, 500);
    }
    const deleteNote = async (nid) => {
        await APIs.deleteNote(nid);
        delete_dialog.value = false;
        setTimeout(loadNotes, 500);
    }
    (async () => await loadNotes())();
</script>

<template>
    <div class="container">
        <template v-if="notes.length > 0" v-for="(note, i) in notes">
            <div class="note">
                <span class="title">{{ note.title }}</span>
                <div class="btns">
                    <v-btn icon="mdi-checkbox-multiple-marked-outline" variant="text" :to="{name: 'Memorize', params: { nid: note.id }}" />
                    <v-btn icon="mdi-text-box-edit-outline" variant="text" :to="{name: 'Edit', params: { nid: note.id }}" />
                    <v-menu>
                        <template v-slot:activator="{ props }">
                            <v-btn icon="mdi-dots-vertical" v-bind="props" variant="text" />
                        </template>
                        <v-list>
                            <v-list-item @click="openRenameDialog(note)">
                                名前の変更
                            </v-list-item>
                            <v-list-item class="text-red" @click="openDeleteDialog(note)">
                                削除
                            </v-list-item>
                        </v-list>
                    </v-menu>
                </div>
            </div>
            <v-divider></v-divider>
        </template>
        <span v-else-if="loading">読込中...</span>
        <span v-else>ノートがありません。ノートを作成してください</span>
    </div>
    <v-dialog v-model="rename_dialog" width="600"> 
        <v-card class="dialog">
            <v-card-title>名前の変更</v-card-title>
            <v-text-field v-model="title" clearable autofocus></v-text-field>
            <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn @click="rename_dialog = false">キャンセル</v-btn>
                <v-btn class="text-red" @click="renameNote(target_id)">決定</v-btn>
            </v-card-actions>
        </v-card>   
    </v-dialog>
    <v-dialog v-model="delete_dialog" width="400">
        <v-card class="dialog">
            <v-card-title>削除</v-card-title>
            <v-card-text>本当に"{{ title }}"を削除しますか？</v-card-text>
            <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn @click="delete_dialog = false">キャンセル</v-btn>
                <v-btn class="text-red" @click="deleteNote(target_id)">削除</v-btn>
            </v-card-actions>
        </v-card>
    </v-dialog>
</template>

<style>
.container{
    min-width: 400px;
    width: 50vw;
    margin: auto;
    margin-top: 20px;
    text-align: center;
}

.title{
    max-width: calc(max(50vw, 400px) - 144px);
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
}

.note{
    display: flex;
    justify-content: space-between;
    align-items: center;
}
.delete{
    color: red;
}
</style>