import type { AxiosResponse } from 'axios';

import { http } from '@/http/http.ts';
import type {IProfile, IProfileUpdate} from "@/types/profile.types.ts";


export const usersService = {
  async getList(): Promise<AxiosResponse<IProfile[]>> {
    return await http.get<IProfile[]>('/user');
  },
  async update(uid: number, data: IProfileUpdate): Promise<AxiosResponse<IProfile>> {
    return await http.patch<IProfile>(`/user/login/${uid}`, data);
  },
  async remove(uid: number): Promise<AxiosResponse<boolean>> {
    return await http.delete<boolean>(`/user/${uid}`);
  },
};
