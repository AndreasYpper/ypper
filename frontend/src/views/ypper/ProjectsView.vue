<template>
  <div class="projects-container">
    <div class="nav-item">
      <div class="link">
        <img src="https://dl.dropboxusercontent.com/s/it0pkztvwiy99jk/maskinnytt.png?dl=0" alt="MaskinNytt" />
      </div>
    </div>
  </div>
</template>

<script>
import stateSite from '@/modules/site'
import { onMounted } from 'vue'
export default {
  setup() {
    const { setSite } = stateSite

    onMounted(() => {
      setSite('ypper')
    })

    return {
      setSite
    }
  }
};
</script>

<style scoped>
.nav-item {
  cursor: pointer;
  border-radius: 15px;
}
.nav-item:hover {
  background-color: #1c3334;
}
.link {
  padding: 10px;
  font-weight: bold;
  text-decoration: none;
  color: #4c9192;
}
.link img {
  width: 10vw;
}
</style>