<script setup lang="ts">

</script>

<template>
<header class="header">
  <div class="container grid">
    <Logo />
    <div class="title">ГБДОУ "Детский сад"</div>
    <TopMenu />
  </div>
</header>
</template>

<style scoped>
.header {
  background-color: var(--color-green);
  height: 60px;
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 5;
  display: flex;
  justify-content: space-between;
  align-items: center;

  @media screen and (min-width: 1024px) {
    height: 80px;
  }
}

.grid {
  display: grid;
  grid-template-columns: 60px 1fr 60px;
}

.title {
  display: flex;
  justify-content: center;
  align-items: center;
  font-family: var(--font-m), sans-serif;
  font-weight: 700;
  font-size: 20px;
  letter-spacing: 0;
  color: white;
}
</style>