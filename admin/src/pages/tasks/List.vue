<script setup lang="ts">
import { onMounted } from 'vue';
import { useTasksStore } from '@/store/tasks.store';

const store = useTasksStore();

onMounted(async () => {
  await store.getList();
})
</script>

<template>
Tasks
</template>

<style scoped>

</style>
