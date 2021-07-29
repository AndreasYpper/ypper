import { ref } from 'vue'

const site = ref('ypper')

function setSite(s) {
  site.value = s
}

function getSite() {
  return site
}

export default { setSite, getSite }