var baseUrl = 'http://127.0.0.1:8000/'
var app = new Vue({
    delimiters: ["[[", "]]"],
    el: '#agent_property',
    data() {
        return {
            fields: ''
        }
    },
    async mounted() {

        await axios.get(baseUrl + 'profile/api/subcategory/').then((resp) => {
            this.fields = resp.data.fields
        })
        document.querySelector('#id_property_type').addEventListener('change', this.property)
        // for create option element otherwise is for update
        if (document.getElementById('id_property_type').value.length == 0) {
            document.getElementById('id_subcategory').innerHTML = ''
            this.create_element('------', '------')

        } else {
            this.update()
        }


    },
    methods: {
        property() {
            document.getElementById('id_subcategory').innerHTML = ''
            this.create_element('------', '------')
            const type = document.getElementById('id_property_type').value
            if (type) {
                this.fields[type].map((e) => {
                    this.create_element(e.obj[0], e.obj[1])
                })
            }

        },
        create_element(value, text) {
            var option = document.createElement('option')
            option.text = text
            option.value = value
            document.getElementById('id_subcategory').appendChild(option)

        },
        update() {
            const type = document.getElementById('id_property_type').value
            const subcategory = document.getElementById('id_subcategory').value

            document.getElementById('id_subcategory').innerHTML = ''
            //Option with the instance option
            this.fields[type].filter((e) => e.obj[0] == subcategory).map((e) => {
                this.create_element(e.obj[0], e.obj[1])
            })
            // Get other options on element
            this.fields[type].filter((e) => e.obj[0] != subcategory).map((e) => {
                this.create_element(e.obj[0], e.obj[1])
            })



        }


    }
})