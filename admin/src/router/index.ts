import { createRouter, createWebHistory } from 'vue-router';

import UsersList from '@/pages/users/List.vue';
import TasksList from '@/pages/tasks/List.vue';
import AuthLogin from '@/pages/auth/Login.vue';

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
    const token = localStorage.getItem('token');

    if (to.meta.requiresAuth && !token) {
        return '/login';
    }
});
