<script setup lang="ts">
</script>

<template>
  <NuxtLayout>
    <NuxtPage />
  </NuxtLayout>
</template>

<style>
@import url('~/assets/styles/main.css');

.page-enter-active, .page-leave-active {
  transition: opacity .5s;
}
.page-enter-from, .page-leave-to {
  opacity: 0;
}
</style>