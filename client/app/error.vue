<script setup lang="ts">
import type {NuxtError} from "#app";

const { error } = defineProps<{ error: NuxtError }>();
</script>

<template>
<div class="page-error">
 <h1>{{error.status}} Not Found</h1>
 <p>{{error.statusText}}</p>
 <button @click="navigateTo('/')">To homepage</button>
</div>
</template>

<style scoped>

</style>