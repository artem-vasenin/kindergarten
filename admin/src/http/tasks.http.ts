import type { AxiosResponse } from 'axios';

import { http } from '@/http/http.ts';
import type { ITask, ITaskCreate, ITaskUpdate } from "@/types/task.types.ts";


export const tasksService = {
  async getList(): Promise<AxiosResponse<ITask[]>> {
    return await http.get<ITask[]>('/task');
  },
  async create(data: ITaskCreate): Promise<AxiosResponse<ITask>> {
    return await http.post<ITask>('/task/', data);
  },
  async update(uid: number, data: ITaskUpdate): Promise<AxiosResponse<ITask>> {
    return await http.patch<ITask>(`/task/${uid}`, data);
  },
  async remove(uid: number): Promise<AxiosResponse<boolean>> {
    return await http.delete<boolean>(`/task/${uid}`);
  },
};
