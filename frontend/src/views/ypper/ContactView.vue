<template>
  <h1>This is contact view</h1>
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
}
</script>

<style>

</style>