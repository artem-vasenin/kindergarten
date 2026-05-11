import { createRouter, createWebHistory } from 'vue-router';
import {useProfileStore} from "@/store/profile.store.ts";

import UsersList from '@/pages/users/List.vue';
import TasksList from '@/pages/tasks/List.vue';
import AuthLogin from '@/pages/auth/Login.vue';
import {RoleType} from "@/types/profile.types.ts";

export const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      name: 'tasks',
      component: TasksList,
      meta: {
        requiresAuth: true,
      },
    },
    {
      path: '/users',
      name: 'users',
      component: UsersList,
      meta: {
        requiresAuth: true,
      },
    },
    {
      path: '/login',
      name: 'login',
      component: AuthLogin,
    },
  ],
});

router.beforeEach((to) => {
    const store = useProfileStore();

    if (to.meta.requiresAuth && (!store.token || store.profile?.role !== RoleType.ADMIN)) {
        return '/login';
    }
});
