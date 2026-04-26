<template>
<div class="layout-default">
  <LayoutHeader />
  <main class="main">
    <slot/>
  </main>
  <LayoutFooter />
</div>
</template>

<style scoped>
.layout-default {
  display: flex;
  flex-direction: column;
  min-height: 100%;
}
.main {
  padding-top: 60px;
  flex: 1;

  @media screen and (min-width: 1024px) {
    padding-top: 80px;
  }
}
</style>