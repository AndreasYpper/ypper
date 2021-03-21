<template>
  <div class="about-container">
    <transition name="content" appear>
      <div class="header">
        <h1>Hi I'm Andreas Ypper</h1>
      </div>
    </transition>
    <transition name="content" appear>
      <div class="content">
        <p>
          I am a hobby full stack developer who loves a challenge. My focus
          right now is in Python, flask, and PostgreSQL for the backend
          development and for the frontend my tools are Vue.js, HTML and CSS.
          When deploying I have mainly used Nginx on Ubuntu. With this said, I'm
          not afraid to learn new things.
          <br /><br />
          <i>What I love in problem solving is the chase to the solution.</i>
        </p>
      </div>
    </transition>
    <transition name="image" appear>
      <div class="image">
        <img src="https://dl.dropboxusercontent.com/s/ixct5jja6n69q97/profile.jpg?dl=0" />
      </div>
    </transition>
  </div>
</template>

<script>
export default {};
</script>

<style scoped>
.about-container {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  grid-template-rows: auto;
}
.header {
  grid-column: 2 / 7;
  grid-row: 1;
}
.content {
  grid-column: 2 / 7;
  grid-row: 2;
  text-align: left;
  font-weight: lighter;
  font-size: 1vw;
}
.content-enter-from {
  opacity: 0;
  transform: translateX(-100px);
}
.content-enter-to {
  opacity: 1;
  transform: translateX(0);
}
.content-enter-active {
  transition: all 1s ease;
}
.content-leave-from {
  opacity: 1;
  transform: translateX(0);
}
.content-leave-to {
  opacity: 0;
  transform: translateX(-100px);
}
.content-leave-active {
  transition: all 1s ease;
}
.image {
  grid-column: 8 / 12;
  grid-row: 2;
  justify-content: center;
}
.image img {
  width: 15vw;
  border-radius: 20px;
}
.image-enter-from {
  opacity: 0;
  transform: translateX(100px);
}
.image-enter-to {
  opacity: 1;
  transform: translateX(0);
}
.image-enter-active {
  transition: all 1s ease;
}
.image-leave-from {
  opacity: 1;
  transform: translateX(0);
}
.image-leave-to {
  opacity: 0;
  transform: translateX(100px);
}
.image-leave-active {
  transition: all 1s ease;
}
</style>