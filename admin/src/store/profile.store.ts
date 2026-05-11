import { ref } from "vue";
import { defineStore } from "pinia";

import { authService } from '@/http/auth.http.ts';
import type { ILogin, IProfile } from '@/types/profile.types.ts';


export const useProfileStore = defineStore("profile", () => {
  const profile = ref<IProfile | null>(null);
  const token = ref<string | null>(null);

  const login = async (payload: ILogin) => {
    const res = await authService.login(payload);
    if (res && res.status === 200 && res.data) {
      token.value = res.data
      localStorage.setItem("token", res.data);
    }
  };
  const logout = () => {
    profile.value = null;
    token.value = null;
    localStorage.removeItem("token");
  };
  const getMe = async () => {
    const res = await authService.getMe();
    if (res && res.status === 200 && res.data) {
      profile.value = { ...profile.value, ...res.data };
    }
  };

  return { profile, token, login, logout, getMe };
});
