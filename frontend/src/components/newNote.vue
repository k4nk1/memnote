<script setup>
import { useUID } from '../composables/useUID';
import { useAPI } from '../composables/useAPI';
import { useRouter } from 'vue-router';

const APIs = useAPI(await useUID());
const nid = await APIs.addNote();
const router = useRouter();
router.replace({ name: 'Note', params: { id: nid}});
</script>

<template>
    <p>ノートを作成中...</p>
</template>

<style scoped>
p{
    text-align: center;
    margin: 20px;
}
</style>