<template>
  <div class="home-container">
    <AboutItem />
  </div>
</template>

<script>
import AboutItem from '@/components/ypper/shared/AboutItem'
import stateSite from '@/modules/site'
import { onMounted } from 'vue'
export default {
  components: {
    AboutItem
  },
  setup() {
    const { setSite } = stateSite

    onMounted(() => {
      setSite('ypper')
    })

    return {
      setSite
    }
  }
}
</script>

<style>

</style>