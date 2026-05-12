import { ref } from "vue";
import { defineStore } from "pinia";

import { usersService } from '@/http/users.http.ts';
import type {IProfile, IProfileUpdate} from '@/types/profile.types.ts';


export const useUsersStore = defineStore("users", () => {
  const list = ref<IProfile[]>([]);

  const getList = async () => {
    const res = await usersService.getList();
    list.value = res.data;
  };
  const update = async (uid: number, data: IProfileUpdate) => {
    await usersService.update(uid, data);
    await getList();
  }
  const remove = async (uid: number) => {
    await usersService.remove(uid);
    await getList();
  }

  return { list, getList, update, remove };
});
