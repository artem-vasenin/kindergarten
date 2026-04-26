<script setup lang="ts">
const open = ref(false);
</script>

<template>
  <div class="menu">
    <button
        :class="['menu__btn', {open}]"
        @click="open = !open"
    ><span class="string"/></button>
    <nav :class="['menu__nav', {open}]">
      <ul class="menu__list">
        <li class="menu__item">
          <NuxtLink to="/about" @click="open = false">О нас</NuxtLink>
        </li>
        <li class="menu__item">
          <NuxtLink to="/staffs" @click="open = false">Коллектив</NuxtLink>
        </li>
        <li class="menu__item">
          <NuxtLink to="/news" @click="open = false">Новости</NuxtLink>
        </li>
        <li class="menu__item">
          <NuxtLink to="/documents" @click="open = false">Документы</NuxtLink>
        </li>
        <li class="menu__item">
          <NuxtLink to="/materials" @click="open = false">Материалы</NuxtLink>
        </li>
        <li class="menu__item">
          <NuxtLink to="/photo" @click="open = false">Фото</NuxtLink>
        </li>
        <li class="menu__item">
          <NuxtLink to="/video" @click="open = false">Видео</NuxtLink>
        </li>
        <li class="menu__item">
          <NuxtLink to="/contacts" @click="open = false">Контакты</NuxtLink>
        </li>
      </ul>
    </nav>
  </div>
</template>

<style scoped>
.menu {
  .string, .string::before, .string::after {
    position: absolute;
    display: inline-block;
    width: 34px;
    height: 4px;
    border-radius: 2px;
    background-color: #fff;
    top: 18px;
    left: 3px;
  }
  .string {
    transition: transform .3s;

    &::before, &::after {
      content: '';
      width: 28px;
      transition: transform .3s;
    }

    &::before {
      top: -12px;
    }

    &::after {
      top: 12px;
    }
  }
  .menu__btn {
    width: 40px;
    height: 40px;
    background-color: transparent;
    border: none;
    cursor: pointer;
    position: relative;
    padding: 0;
    margin: 0;

    &.open {
      .string {
        transform: rotate(45deg);
        transition: transform .3s;

        &::before {
          top: 0;
          left: 0;
          width: 34px;
          transform: rotate(90deg);
          transition: transform .3s;
        }
        &::after {
          top: 0;
          display: none;
        }
      }
    }
  }

  .menu__nav {
    position: fixed;
    top: 60px;
    left: 100%;
    right: -100%;
    bottom: 0;
    background-color: var(--color-green);
    transition: left .3s, right .3s;
    border-top: 4px solid white;

    &.open {
      left: 0;
      right: 0;
      transition: left .3s, right .3s;
    }
  }
  .menu__list {
    margin: 0;
    padding: 100px 0 0;
    list-style: none;
    width: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  .menu__item {
    font-weight: 700;
    font-size: 20px;
    line-height: 26px;
    margin-bottom: 16px;

    a {
      color: white;
      text-decoration: none;
      transition: color .2s;

      &:hover, &:active {
        color: var(--color-red-dark);
        transition: color .2s;
      }
      &:visited {
        color: white;
      }
    }
  }
}
</style>