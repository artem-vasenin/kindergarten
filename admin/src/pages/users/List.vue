<script setup lang="ts">
import {onMounted, ref} from 'vue';

import Item from './Item.vue';
import { usersService } from '@/http/users.http';
import {useUsersStore} from '@/store/users.store.ts';
import {RoleType} from "@/types/profile.types.ts";

const store = useUsersStore();
const edit = ref<boolean>(false);
const email = ref<string>('');
const password = ref<string>('');
const role = ref<RoleType>(RoleType.GUEST);

const cancel = () => {
  edit.value = false;
  email.value = '';
  password.value = '';
  role.value = RoleType.GUEST;
};

const save = async (e: Event) => {
  e.preventDefault();
  const e_val = email.value.trim().toLowerCase();
  const p_val = password.value.trim();

  if (!e_val || !p_val) return;

  try {
    await usersService.create({ email: e_val, password: p_val, role: role.value });
    await store.getList();
    cancel();
  } catch (e) {
    console.log(e);
  }
};

onMounted(async () => {
  await store.getList();
});
</script>

<template>
<div class="wrap">
  <h1 class="title">
    <span>Users</span>
    <button class="btn btn_add" @click="edit = true">+</button>
  </h1>

  <div class="content">
    <Item v-for="i in store.list" :key="i.id" :item="i" />
  </div>

  <div class="modal" v-if="edit">
    <form class="form" @submit="save">
      <h3 class="form_title">Create User</h3>
      <input placeholder="Email" type="email" class="input" required v-model="email">
      <input placeholder="Password" type="password" class="input" required v-model="password">
      <select v-model="role" class="select">
        <option value="guest">Guest</option>
        <option value="admin">Admin</option>
      </select>
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
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
  grid-gap: 12px;
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
