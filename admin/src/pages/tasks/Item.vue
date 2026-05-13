<script setup lang="ts">
import { ref } from 'vue';

import type { ITask } from "@/types/task.types.ts";
import { useUsersStore } from '@/store/users.store.ts';
import { useTasksStore } from '@/store/tasks.store.ts';
import type { IProfile } from "@/types/profile.types.ts";
import { tasksService } from '@/http/tasks.http';

const props = defineProps<{ item: ITask }>();
const userStore = useUsersStore();
const taskStore = useTasksStore();

const edit = ref<boolean>(false);
const name = ref<string>(props.item.name);
const desc = ref<string>(props.item.description);

const clear = () => {
  name.value = props.item.name;
  desc.value = props.item.description;
};

const getUser = () => {
  const user: IProfile | undefined = userStore.list.find(u => u.id === props.item.user_id);
  return user ? `${user.email} (${user.role})` : props.item.user_id;
}

const check = async () => {
  try {
    await tasksService.update(props.item.id, { checked: !props.item.checked });
    await taskStore.getList();
  } catch (e) {
    console.error(e);
  }
};

const del = async () => {
  try {
    await tasksService.remove(props.item.id);
    await taskStore.getList();
  } catch (e) {
    console.error(e);
  }
};

const save = async () => {
  if (!name.value.trim()) return;
  try {
    await tasksService.update(
      props.item.id,
      { name: name.value.trim(), description: desc.value.trim() },
    );
    await taskStore.getList();
    clear();
    edit.value = false;
  } catch (e) {
    console.error(e);
  }
};
</script>

<template>
  <div class="wrap" :class="{active: props.item.checked}">
    <div class="check">
      <button class="btn btn_check" @click="check"/>
    </div>
    <div class="user">{{getUser()}}</div>
    <div class="content">
      <div class="top">
        <span v-if="!edit">{{props.item.name}}</span>
        <input v-else type="text" class="input" v-model="name">
      </div>
      <div class="bottom">
        <span v-if="!edit">{{props.item.description}}</span>
        <input v-else type="text" class="input" v-model="desc">
      </div>
    </div>
    <div class="actions">
      <template v-if="!edit">
        <button class="btn btn_edit" @click="edit = !edit"/>
        <button class="btn btn_delete" @click="del"/>
      </template>
      <button v-else class="btn btn_save" @click="save"/>
    </div>
  </div>
</template>

<style scoped>
.wrap {
  display: flex;
  gap: 20px;
  width: 100%;
  margin-bottom: 20px;
  background-color: var(--color-gray-dark);
  border: 1px solid var(--color-dark);
  border-radius: 4px;
  padding: 8px 8px 8px 0;
  box-shadow: 2px 2px 4px var(--color-dark-a2);

  &.active {
    .btn_check {
      background: var(--color-green-light);
      box-shadow: 1px 1px 2px var(--color-green) inset, 1px 1px 4px var(--color-dark-a3);
    }
    .user {
      background-color: var(--color-green);
      box-shadow: 1px 1px 4px var(--color-green-light);
    }
    .top {
      text-decoration: line-through;
    }
  }
}
.check {
  flex: 0 0 40px;
  max-width: 40px;
  border-right: 1px solid var(--color-gray);
  display: flex;
  align-items: center;
  justify-content: center;
}
.content {
  flex: 1;
  display: flex;
  flex-direction: column;
}
.top {
  display: flex;
  align-items: center;
  gap: 12px;
  flex: 1;
  padding-bottom: 4px;
}
.user {
  align-self: center;
  background-color: var(--color-dark);
  color: white;
  font-size: 12px;
  display: inline-flex;
  padding: 6px 8px;
  border-radius: 4px;
  line-height: 1;
  box-shadow: 2px 2px 4px var(--color-dark-a5);
}
.bottom {
  flex: 1;
  padding-top: 4px;
  border-top: 1px solid var(--color-gray);
}
.actions {
  flex: 0 0 50px;
  max-width: 50px;
  border-left: 1px solid var(--color-gray);
  position: relative;
  height: 40px;
  filter: drop-shadow(0 0 4px var(--color-dark-a3));
}
.btn {
  border: none;
  background: none;
  cursor: pointer;

  &.btn_check {
    width: 20px;
    height: 20px;
    background: white;
    border-radius: 50%;
    border: 2px solid var(--color-gray);
    box-shadow: 1px 1px 2px var(--color-dark-a5) inset, 1px 1px 4px var(--color-dark-a3);
  }

  &.btn_edit {
    width: 30px;
    height: 30px;
    border: none;
    background: var(--color-green);
    transition: background .2s;
    clip-path: polygon(100% 0, 0 0, 100% 100%);
    position: absolute;
    top: 0;
    right: 0;

    &:hover {
      background: var(--color-green-light);
      transition: background .2s;
    }
  }

  &.btn_delete {
    width: 30px;
    height: 30px;
    border: none;
    background: var(--color-red);
    transition: background .2s;
    clip-path: polygon(0 0, 0 100%, 100% 100%);
    position: absolute;
    top: 10px;
    right: 10px;

    &:hover {
      background: var(--color-red-light);
      transition: background .2s;
    }
  }

  &.btn_save {
    width: 34px;
    height: 34px;
    background-color: var(--color-green);
    box-shadow: 2px 2px 4px var(--color-dark-a3);
    position: absolute;
    top: 2px;
    right: 2px;
    transition: background .2s;
    border-radius: 4px;

    &:hover {
      background: var(--color-green-light);
      transition: background .2s;
      box-shadow: 1px 1px 4px var(--color-green-light);
    }
  }
}
.input {
  border: none;
  background: var(--color-gray);
  width: 100%;
  padding: 0;
  font-size: 15px;
  height: 18px;
  outline: none;
}
</style>
