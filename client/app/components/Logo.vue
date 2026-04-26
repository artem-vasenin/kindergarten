<template>
<NuxtImg
    src="/logo.png"
    width="45"
    height="62"
    alt="logo"
    class="logo__img"
    @click="navigateTo('/')"
  />
</template>

<style scoped>
.logo__img {
  @media screen and (max-width: 1024px) {
    width: 30px;
    height: 40px;
  }
}
</style>