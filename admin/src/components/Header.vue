<script setup lang="ts">
  import { useRouter } from 'vue-router';
  import {useProfileStore} from "@/store/profile.store.ts";

  const store = useProfileStore();
  const router = useRouter();

  const logout = async () => {
    store.logout();
    await router.push("/login");
  };
</script>

<template>
  <header class="header">
    <nav class="nav container">
      <div class="logo">
        ToDo
      </div>
      <ul class="menu">
        <template v-if="store.token">
          <li class="menu_item">
            <RouterLink to="/" class="menu_link">Tasks</RouterLink>
          </li>
          <li class="menu_item">
            <RouterLink to="/users" class="menu_link">Users</RouterLink>
          </li>
          <li class="menu_item">
            <span class="menu_link" @click="logout">Logout</span>
          </li>
        </template>
        <li class="menu_item" v-else>
          <RouterLink to="/login" class="menu_link">Login</RouterLink>
        </li>
      </ul>
    </nav>
  </header>
</template>

<style scoped>
  .header {
    background-color: var(--color-dark);
    height: 60px;
    box-shadow: 0 0 12px 0 var(--color-dark);
  }
  .logo {
    font-size: 22px;
    color: white;
    font-weight: bold;
  }
  .nav {
    display: flex;
    align-items: center;
    gap: 40px;
    height: 100%;
  }
  .menu {
    margin: 0;
    padding: 0;
    list-style: none;
    display: flex;
    align-items: center;
    justify-content: flex-end;
    gap: 12px;
    flex: 1;
  }
  .menu_link {
    text-decoration: none;
    color: white;
    font-size: 22px;
    font-weight: 100;
    cursor: pointer;

    &.router-link-exact-active {
      color: var(--color-yellow-light);
      text-shadow: 0 0 2px var(--color-yellow-light);
    }
  }
</style>
