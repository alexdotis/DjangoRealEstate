var app = new Vue({
    delimiters: ["[[", "]]"],
    el: '#vue-app',
    data() {
        return {
            option: '',
            fields: ''
        }
    },
    mounted() {
        document.querySelector('#id_type').addEventListener('change', this.property)
        document.getElementById('id_subcategory').innerHTML = ''
        this.create_element('------', '------')
        axios.get('http://127.0.0.1:8000/listing/api/subcategory/').then((resp) => {
            this.fields = resp.data.fields
        })


    },
    methods: {
        property() {
            document.getElementById('id_subcategory').innerHTML = ''
            this.create_element('------', '------')
            this.option = document.getElementById('id_type').value
            if (this.option) {
                this.fields[this.option].map((e) => {
                    this.create_element(e.obj[0], e.obj[1])
                })
            }

        },
        create_element(value, text) {
            var option = document.createElement('option')
            option.text = text
            option.value = value
            document.getElementById('id_subcategory').appendChild(option)

        }


    }
})