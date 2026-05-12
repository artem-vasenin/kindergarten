<script setup lang="ts">
import { defineProps, ref } from 'vue';

import {type IProfile, RoleType} from '@/types/profile.types';

const props = defineProps<{ item: IProfile }>();
const edit = ref<boolean>(false);
const email = ref<string>(props.item.email);
const role = ref<RoleType>(props.item.role);
</script>

<template>
<div class="item">
  <div class="actions-top">
    <button class="btn btn_edit" @click="edit = !edit">{{edit ? 'Отменить' : 'Изменить'}}</button>
    <button class="btn btn_del" :disabled="edit">Удалить</button>
  </div>
  <div class="row row_id">
    <span class="label">ID</span>
    <span class="value">{{props.item.id}}</span>
  </div>
  <div class="row row_email">
    <span class="label">Email</span>
    <span v-if="!edit" class="value">{{props.item.email}}</span>
    <input v-else type="text" class="input" v-model="email">
  </div>
  <div class="row row_role">
    <span class="label">Role</span>
    <span v-if="!edit" class="value">{{props.item.role}}</span>
    <input v-else type="text" class="input" v-model="role">
  </div>
  <div class="actions-bottom">
    <button v-if="edit" class="btn btn_save">Сохранить</button>
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
  min-height: 200px;
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
}
.input {
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
