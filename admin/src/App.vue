<script setup lang="ts">
import Header from '@/components/Header.vue';
</script>

<template>
  <section>
    <Header />
    <main class="main">
      <div class="container">
        <router-view />
      </div>
    </main>
  </section>
</template>

<style>
  :root {
    --color-gray: #bbb;
    --color-gray-dark: #999;
    --color-dark-light: #666;
    --color-dark: #333;
    --color-red-light: #ff4545;
    --color-red: #800101;
    --color-green-light: #82dd0d;
    --color-green: #3f6c00;
    --color-yellow-light: #ffdf6b;
    --color-yellow: #cca600;

    --color-dark-a7: rgba(0, 0, 0, 0.7);
  }
  * {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
  }
  html, body {
    height: 100%;
  }
  .container {
    min-width: 320px;
    max-width: 1280px;
    width: 100%;
    margin: 0 auto;
    padding: 0 12px;
  }
</style>
