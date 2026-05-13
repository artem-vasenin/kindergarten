<script setup lang="ts">
import { defineProps, ref } from 'vue';

import {type IProfile, RoleType} from '@/types/profile.types';
import { usersService } from '@/http/users.http';
import {useUsersStore} from "@/store/users.store.ts";

const store = useUsersStore();
const props = defineProps<{ item: IProfile }>();
const edit = ref<boolean>(false);
const password = ref<string>('');
const role = ref<RoleType>(props.item.role);

const toggle = () => {
  edit.value = !edit.value;
  role.value = props.item.role;
  password.value = ''
}

const save = async () => {
  try {
    await usersService.update(props.item.id, { role: role.value, password: password.value });
    await store.getList();
    toggle();
  } catch (e) {
    console.error(e);
  }
};

const remove = async () => {
  try {
    await usersService.remove(props.item.id);
    await store.getList();
  } catch (e) {
    console.error(e);
  }
};
</script>

<template>
<div class="item">
  <div class="actions-top">
    <button class="btn btn_edit" @click="toggle">{{edit ? 'Отменить' : 'Изменить'}}</button>
    <button class="btn btn_del" :disabled="edit" @click="remove">Удалить</button>
  </div>
  <div class="row row_id">
    <span class="label">ID</span>
    <span class="value">{{props.item.id}}</span>
  </div>
  <div class="row row_email">
    <span class="label">Email</span>
    <span class="value">{{props.item.email}}</span>
  </div>
  <div class="row row_role">
    <span class="label">Role</span>
    <span v-if="!edit" class="value">{{props.item.role}}</span>
    <select v-else v-model="role" class="select">
      <option value="admin">Admin</option>
      <option value="guest">Guest</option>
    </select>
  </div>
  <div class="row row_role">
    <span v-if="edit" class="label">Password</span>
    <input v-if="edit" type="text" class="input" v-model="password">
  </div>
  <div class="actions-bottom">
    <button v-if="edit" class="btn btn_save" @click="save">Сохранить</button>
  </div>
</div>
</template>

<style scoped>
.item {
  background-color: var(--color-dark-light);
  border-radius: 8px;
  padding: 16px;
  display: flex;
  flex-direction: column;
  min-height: 230px;
  box-shadow: 2px 2px 6px rgb(0 0 0 / 50%);
}
.actions-top, .actions-bottom {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 20px;
  gap: 16px;
}
.actions-bottom {
  margin-top: 20px;
  margin-bottom: 0;
  height: 30px;
}
.btn {
  border: none;
  border-radius: 4px;
  background-color: transparent;
  margin: 0;
  padding: 0;
  cursor: pointer;
  flex: 1;
  height: 30px;
  color: white;
  text-transform: uppercase;
  font-size: 11px;

  &.btn_edit {
    background-color: var(--color-yellow);
  }
  &.btn_del {
    background-color: var(--color-red);
  }
  &.btn_save {
    background-color: var(--color-green);
  }
}
.row {
  flex: 1;
  display: flex;
  justify-content: space-between;
  align-items: center;
  color: white;
  height: 26px;
}
.label {
  flex: 0 0 70px;
}
.value, .input, .select {
  flex: calc(100% - 70px);
  max-width: calc(100% - 70px);
  text-align: right;
}
.input, .select {
  background-color: transparent;
  border: none;
  outline: none;
  border-bottom: 1px solid var(--color-dark);
  color: white;
  text-align: right;
  font-size: 16px;
  font-family: "Times New Roman", sans-serif;
}
</style>
