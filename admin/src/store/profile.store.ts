import { ref } from "vue";
import { defineStore } from "pinia";

import { authService } from '@/http/auth.http.ts';
import { useTasksStore } from '@/store/tasks.store.ts';
import { useUsersStore } from '@/store/users.store.ts';
import type { ILogin, IProfile } from '@/types/profile.types.ts';


export const useProfileStore = defineStore("profile", () => {
  const profile = ref<IProfile | null>(null);
  const token = ref<string | null>(null);
  const userStore = useTasksStore();
  const tasksStore = useUsersStore();

  const login = async (payload: ILogin) => {
    const res = await authService.login(payload);
    if (res && res.status === 200 && res.data) {
      token.value = res.data
    }
    await getMe();
  };
  const logout = () => {
    profile.value = null;
    token.value = null;
    userStore.clear();
    tasksStore.clear();
  };
  const getMe = async () => {
    const res = await authService.getMe();
    if (res && res.status === 200 && res.data) {
      profile.value = { ...profile.value, ...res.data };
    }
  };

  return { profile, token, login, logout, getMe };
}, { persist: true });
