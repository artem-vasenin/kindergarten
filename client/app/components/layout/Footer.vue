<script setup lang="ts">

</script>

<template>
<footer class="footer">
  <div class="container grid">
    <div class="footer__icons">
      <Logo class="logo" />
      <ul class="icons">
        <li class="icon">
          <NuxtLink href="https://vk.com" class="icon__link"><IconVK /></NuxtLink>
        </li>
        <li class="icon">
          <NuxtLink href="https://vk.com" class="icon__link"><IconVK /></NuxtLink>
        </li>
        <li class="icon">
          <NuxtLink href="https://vk.com" class="icon__link"><IconVK /></NuxtLink>
        </li>
      </ul>
    </div>
    <div class="footer__menu">
      <ul class="menu">
        <li class="menu__item">
          <NuxtLink to="/about" class="menu__link">О нас</NuxtLink>
        </li>
        <li class="menu__item">
          <NuxtLink to="/about" class="menu__link">Образование и воспитание</NuxtLink>
        </li>
        <li class="menu__item">
          <NuxtLink to="/about" class="menu__link">Родителям</NuxtLink>
        </li>
        <li class="menu__item">
          <NuxtLink to="/about" class="menu__link">Галерея</NuxtLink>
        </li>
      </ul>
    </div>
    <div class="footer__contacts">
      <ul class="contacts">
        <li class="contact">г. Москва, ул. Московcкая, д. 32</li>
        <li class="contact">Пн-Пт с 8:00 до 20:00</li>
        <li class="contact">
          <NuxtLink href="tel:+79999999999" class="menu__link">+7(999)999 99 99</NuxtLink>
        </li>
        <li class="contact">
          <NuxtLink href="mailto:MoskowDS@gmail.ru" class="menu__link">MoskowDS@gmail.ru</NuxtLink>
        </li>
      </ul>
    </div>
  </div>
</footer>
</template>

<style scoped>
.footer {
  background-color: var(--color-green);
  padding: 10px 0 14px;

  @media screen and (min-width: 1024px) {
    padding: 34px 0 47px;
  }
}
.grid {
  display: flex;
  flex-direction: column-reverse;
  align-items: center;

  @media screen and (min-width: 1024px) {
    flex-direction: row;
    justify-content: space-between;
  }
}
.logo {
  display: none;

  @media screen and (min-width: 1024px) {
    display: initial;
    margin-bottom: 34px;
  }
}
.icons {
  padding: 0;
  margin: 0;
  list-style: none;
  display: flex;
  gap: 10px;
}
.icon__link {
  text-decoration: none;
  display: inline-flex;
  justify-content: center;
  align-items: center;
  width: 20px;
  height: 20px;
  border-radius: 50%;
  font-size: 16px;
  background-color: var(--color-yellow);
  transition: box-shadow .2s;

  @media screen and (min-width: 1024px) {
    width: 40px;
    height: 40px;
    font-size: 26px;
  }

  &:hover {
    box-shadow: 0 0 6px rgb(0 0 0 /.4);
    transition: box-shadow .2s;
  }
}

.footer__menu {
  display: none;

  @media screen and (min-width: 1024px) {
    display: initial;
  }
}
.menu {
  margin: 0;
  padding: 0;
  list-style: none;
}
.menu__item {
  margin-bottom: 12px;

  &:last-child {
    margin-bottom: 0;
  }
}
.menu__link {
  color: white;
  text-align: center;
  font-weight: 700;
  font-size: 12px;
  line-height: 1.2;
  text-decoration: none;
  transition: color .2s;

  @media screen and (min-width: 1024px) {
    font-size: 20px;
  }

  &:hover {
    color: var(--color-red-dark);
    transition: color .2s;
  }
}

.contacts {
  padding: 0 0 10px;
  margin: 0;
  list-style: none;
}
.contact {
  color: white;
  text-align: center;
  font-weight: 700;
  font-size: 12px;
  line-height: 1.2;

  @media screen and (min-width: 1024px) {
    font-size: 20px;
    margin-bottom: 12px;
    text-align: initial;

    &:last-child {
      margin-bottom: 0;
    }
  }
}
</style>