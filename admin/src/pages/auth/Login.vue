<script setup lang="ts">
import { ref } from "vue";
import { useRouter } from 'vue-router';
import { useProfileStore } from "@/store/profile.store.ts";

const store = useProfileStore();
const router = useRouter();

const email = ref("");
const password = ref("");

const submit = async (e: any) => {
  e.preventDefault();

  if (!email.value.trim() || !password.value.trim()) {
    return;
  }
  try {
    const loginRes = await store.login({ email: email.value, password: password.value });
    const meRes = await store.getMe();
    console.log(meRes, loginRes);
    await router.push("/");
  } catch (e) {
    console.error(e);
  }
};
</script>

<template>
<div class="wrap">
  <div class="content">
    <form class="form" @submit="submit" autocomplete="off">
      <h1 class="title">Админ панель</h1>

      <div class="form_field">
        <input type="email" class="form_input" v-model="email" autocomplete="off" />
      </div>
      <div class="form_field">
        <input type="password" class="form_input" v-model="password" autocomplete="off" />
      </div>
      <div class="fom_actions">
        <button class="btn" type="submit">Войти</button>
      </div>
    </form>
  </div>
</div>
</template>

<style scoped>
.wrap {
  height: calc(100vh - 60px);
  display: flex;
  justify-content: center;
  align-items: center;
}
.form {
  width: 600px;
  height: 320px;
  background-color: var(--color-dark);
  border-radius: 4px;
  padding: 20px;
}
.title {
  text-align: center;
  color: white;
  margin-bottom: 40px;
  font-size: 20px;
  text-transform: uppercase;
}
.form_field {
  padding-bottom: 40px;
}
.form_input {
  width: 100%;
  height: 40px;
  background-color: white!important;
  border: none;
  outline: none;
  padding: 16px;
  text-align: center;
  font-size: 20px!important;
  border-radius: 4px;
}
.btn {
  width: 100%;
  height: 40px;
  background-color: black;
  border: 1px solid var(--color-dark-light);
  border-radius: 4px;
  color: white;
  font-size: 20px;
  text-transform: uppercase;
  cursor: pointer;

  &:hover {
    color: var(--color-green-light);
    border-color: var(--color-green);
  }
}
</style>
