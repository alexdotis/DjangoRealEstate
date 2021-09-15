var app = new Vue({
    el: '#images_settings',
    delimiters: ['[[', ']]'],
    data() {
        return {
            prefixes: [],
            countPrefix: 3,
        }
    },
    methods: {
        imagesForm() {
            const schema = {
                labelID: `id_listingimages_set-${this.countPrefix}-image`,
                inputID: `id_listingimages_set-${this.countPrefix}-image`,
                inputName: `listingimages_set-${this.countPrefix}-image`,
                hiddenInputID: `id_listingimages_set-${this.countPrefix}-id`,
                hiddenInputName: `listingimages_set-${this.countPrefix}-id`,
                hiddenInputListing: `id_listingimages_set-${this.countPrefix}-listing`,
                hiddenInputListingName: `listingimages_set-${this.countPrefix}-listing`
            }
            this.prefixes.push(schema)
            this.countPrefix += 1
            document.getElementById('id_listingimages_set-TOTAL_FORMS').setAttribute('value', this
                .countPrefix)
        }
    }


})