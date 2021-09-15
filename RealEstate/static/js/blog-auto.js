var baseUrl = 'http://127.0.0.1:8000/'
var app = new Vue({
    el: '#auto',
    delimiters: ['[[', ']]'],
    data() {
        return {
            data: [],
            filterInput: null,
            errors:null
        }
    },
    computed: {
        match() {
            return this.data.filter(e => e.title.toLowerCase().indexOf(this.filterInput) > -1)
        }
    },
    mounted() {
        axios.get(baseUrl + 'blogs/api/').then(resp => {
            this.data = resp.data
        })
    },
    methods: {
        goto() {
            const slug = this.data.filter(e => e.title.toLowerCase().indexOf(this.filterInput.toLowerCase()) > -1).map(e => e.slug)
            if (slug.length > 0) {
                window.location.href = baseUrl + 'blogs/' + slug.join(' ')
            }else{
                this.errors = 'There is not such a blog'
            }

        }
    }

})