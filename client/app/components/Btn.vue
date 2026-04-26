<script setup lang="ts">
const { size = 'md', block = false } = defineProps<{
  size: 'xl' | 'md';
  block: boolean;
}>();
</script>

<template>
<button
  :class="['btn', size, { block }]"
><slot /></button>
</template>

<style scoped>
.btn {
  border: none;
  border-radius: 50px;
  background-color: var(--color-red-light);
  color: white;
  font-family: var(--font-n), sans-serif;
  font-weight: 700;
  letter-spacing: 0;
  text-align: center;
  line-height: 1;
  display: inline-flex;
  justify-content: center;
  align-items: center;
  cursor: pointer;
  transition: background-color .3s;

  &:hover {
    background-color: var(--color-red);
    transition: background-color .3s;
  }

  &:active {
    background-color: var(--color-red-dark);
    transition: background-color .3s;
  }

  &.md {
    height: 42px;
    min-width: 270px;
    font-size: 24px;
  }
  &.xl {
    height: 62px;
    min-width: 400px;
    font-size: 46px;
  }
  &.block {
    width: 100%;
  }
}
</style>