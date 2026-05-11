import { http } from '@/http/http.ts';
import type {ILogin} from "@/types/profile.types.ts";

export const authService = {
  async login(data: ILogin) {
    try {
      return await http.post('/auth/login', data);
    } catch (e) {
      console.error(e);
    }
  },
  async getProfile(uid: number) {
    try {
      return await http.get('/user/' + uid);
    } catch (e) {
      console.error(e);
    }
  },
};
