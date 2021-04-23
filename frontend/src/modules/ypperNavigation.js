import { reactive } from 'vue'

const navigation = reactive({
  nav: ''
})

function setNav(nav) {
  navigation.nav = nav
}

function getNav() {
  return navigation
}

export default { setNav, getNav}