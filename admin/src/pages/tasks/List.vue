<script setup lang="ts">
import {onMounted, ref} from 'vue';

import Item from "@/pages/tasks/Item.vue";
import { useTasksStore } from '@/store/tasks.store';
import { useUsersStore } from '@/store/users.store';
import { tasksService } from "@/http/tasks.http.ts";

const store = useTasksStore();
const userStore = useUsersStore();
const edit = ref<boolean>(false);
const name = ref<string>('');
const description = ref<string>('');
const checked = ref<boolean>(false);
const user_id = ref<number | null>(null);

const cancel = () => {
  edit.value = false;
  name.value = '';
  description.value = '';
  checked.value = false;
  user_id.value = null;
};

const save = async (e: Event) => {
  e.preventDefault();
  const n_val = name.value.trim();
  const d_val = description.value.trim();

  if (!n_val) return;

  try {
    await tasksService.create({
      name: n_val,
      description: d_val,
      checked: checked.value,
    });
    await store.getList();
    cancel();
  } catch (e) {
    console.log(e);
  }
};

onMounted(async () => {
  await userStore.getList();
  await store.getList();
})
</script>

<template>
<div class="wrap">
  <h1 class="title">
    <span>Tasks</span>
    <button class="btn btn_add" @click="edit = true">+</button>
  </h1>

  <div class="content">
    <Item v-for="i in store.list" :key="i.id" :item="i" />
  </div>

  <div class="modal" v-if="edit">
    <form class="form" @submit="save">
      <h3 class="form_title">Create Task</h3>
      <input placeholder="Name" type="text" class="input" required v-model="name">
      <input placeholder="Description" type="text" class="input" v-model="description">
      <select v-model="user_id" class="select">
        <option :value="i.id" v-for="i in userStore.list">{{i.email}} - {{i.role}}</option>
      </select>
      <label class="label">
        <input type="checkbox" v-model="checked"> Checked
      </label>
      <div class="actions">
        <button class="btn btn_cancel" @click="cancel">Cancel</button>
        <button class="btn btn_save" type="submit">Save</button>
      </div>
    </form>
  </div>
</div>
</template>

<style scoped>
.title {
  margin-top: 40px;
  text-align: center;
  margin-bottom: 40px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.content {
}

.modal {
  position: fixed;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  z-index: 1;
  background-color: var(--color-dark-a7);
  display: flex;
  justify-content: center;
  align-items: center;
}
.form {
  width: 600px;
  height: 360px;
  background: white;
  border-radius: 8px;
  padding: 40px 20px;
  display: flex;
  flex-direction: column;
}
.form_title {
  text-align: center;
  margin-bottom: 40px;
  text-transform: uppercase;
}
.input {
  width: 100%;
  height: 40px;
  margin-bottom: 20px;
  padding: 8px;
}
.select {
  width: 100%;
  height: 40px;
  padding: 8px;
  margin-bottom: 20px;
}
.label {
  margin-bottom: 20px;
}
.actions {
  flex: 1;
  align-content: flex-end;
  display: flex;
  justify-content: space-between;
}
.btn {
  border: none;
  background: none;
  height: 40px;
  min-width: 100px;
  box-shadow: 0 0 6px var(--color-dark-a7);
  border-radius: 4px;
  cursor: pointer;
  text-transform: uppercase;

  &:hover {
    box-shadow: 0 0 2px var(--color-dark-a7);
  }

  &.btn_save {
    background: var(--color-green);
    color: white;
  }

  &.btn_add {
    background: var(--color-green);
    color: white;
    font-size: 26px;
    line-height: 1;
  }
}
</style>
