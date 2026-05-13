<script setup lang="ts">
import { onMounted } from 'vue';
import { useUsersStore } from '@/store/users.store.ts';
import Item from './Item.vue';

const store = useUsersStore();

onMounted(() => {
  store.getList();
});
</script>

<template>
<div class="wrap">
  <h1 class="title">Users</h1>

  <div class="content">
    <Item v-for="i in store.list" :key="i.id" :item="i" />
</div>
</div>
</template>

<style scoped>
.title {
  margin-top: 40px;
  text-align: center;
  margin-bottom: 40px;
}
.content {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
  grid-gap: 12px;
}
</style>
