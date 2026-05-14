import { ref } from "vue";
import { defineStore } from "pinia";

import { usersService } from '@/http/users.http.ts';
import type { IProfile } from '@/types/profile.types.ts';


export const useUsersStore = defineStore("users", () => {
  const list = ref<IProfile[]>([]);

  const getList = async () => {
    const res = await usersService.getList();
    list.value = res.data;
  };

  const clear = () => {
    list.value = [];
  };

  return { list, getList, clear };
}, { persist: true });
