import { http } from '@/http/http.ts';
import type {ILogin} from "@/types/profile.types.ts";

export const authService = {
  async login(data: ILogin) {
    try {
      return await http.post('/user/login', data);
    } catch (e) {
      console.error(e);
    }
  },
  async getMe() {
    try {
      return await http.get('/user/me');
    } catch (e) {
      console.error(e);
    }
  },
};
