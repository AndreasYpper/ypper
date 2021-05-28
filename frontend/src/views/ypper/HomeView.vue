<template>
  <div class="home-container">
    <div v-if="nav.nav == 'home'">
      <AboutItem />
    </div>
    <div v-if="nav.nav == 'contact'">
      <ContactItem />
    </div>
    <div v-if="nav.nav == 'projects'">
      <ProjectsView />
    </div>
  </div>
</template>

<script>
import AboutItem from '@/components/ypper/shared/AboutItem'
import ContactItem from '@/components/ypper/shared/ContactItem'
import ProjectsView from '@/components/ypper/shared/ProjectsView'
import stateSite from '@/modules/site'
import stateNavigation from '@/modules/ypperNavigation'
import { onMounted } from 'vue'
export default {
  components: {
    AboutItem,
    ContactItem,
    ProjectsView
  },
  setup() {
    const { setSite } = stateSite
    const { getNav } = stateNavigation
    const nav = getNav()

    onMounted(() => {
      setSite('ypper')
    })

    return {
      setSite,
      nav
    }
  }
}
</script>

<style>

</style>