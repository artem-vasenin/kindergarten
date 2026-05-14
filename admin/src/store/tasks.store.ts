import { ref } from "vue";
import { defineStore } from "pinia";

import { tasksService } from '@/http/tasks.http.ts';
import type { ITask } from '@/types/task.types.ts';


export const useTasksStore = defineStore("tasks", () => {
  const list = ref<ITask[]>([]);

  const getList = async () => {
    const res = await tasksService.getList();
    list.value = res.data;
  };

  const clear = () => {
    list.value = [];
  };

  return { list, getList, clear };
});
