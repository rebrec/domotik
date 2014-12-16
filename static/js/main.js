$().ready(function(){

    $('.btn-toggle').click(function() {
        $(this).find('.btn').toggleClass('active');
        $(this).find('.btn').toggleClass('btn-primary');
        $(this).find('.btn').toggleClass('btn-default');
        $sensor = $(this).data("sensor");

        $.get(
            'inter/set/?name=' + $sensor + '&cmd=toggle', // Le fichier cible côté serveur.
            'false', // Nous utilisons false, pour dire que nous n'envoyons pas de données.
            function (state){},
            'json' // Format des données reçues.
            );
    });

    setInterval(function update_data(){
        $.get(
            'inter/get/?name=LampeDevant', // Le fichier cible côté serveur.
            'false', // Nous utilisons false, pour dire que nous n'envoyons pas de données.
            function (data){
                console.log(data);
                if (data['state'] == true){
                    $('.lampedevant:contains("ON")').addClass('active');
                    $('.lampedevant:contains("ON")').addClass('btn-primary');
                    $('.lampedevant:contains("ON")').removeClass('default');
                    $('.lampedevant:contains("OFF")').removeClass('active');
                    $('.lampedevant:contains("OFF")').removeClass('btn-primary');
                    $('.lampedevant:contains("OFF")').addClass('default');

                } else {
                    $('.lampedevant:contains("OF")').addClass('active');
                    $('.lampedevant:contains("OF")').addClass('btn-primary');
                    $('.lampedevant:contains("OF")').removeClass('default');
                    $('.lampedevant:contains("ON")').removeClass('active');
                    $('.lampedevant:contains("ON")').removeClass('btn-primary');
                    $('.lampedevant:contains("ON")').addClass('default');
                }

            },
            'json' // Format des données reçues.
        );
    },2000);

/***************************************************************************/
    $('#lampedevant').click(function(){
        $('#lampedevant').toggleClass('on');
        $('#lampedevant').toggleClass('off');

        $.get(
            'inter/set/?name=LampeDevant&cmd=toggle', // Le fichier cible côté serveur.
            'false', // Nous utilisons false, pour dire que nous n'envoyons pas de données.
            function (state){},
            'json' // Format des données reçues.
            );
    });


    setInterval(function update_data(){
        $.get(
            'inter/get/?name=LampeDevant', // Le fichier cible côté serveur.
            'false', // Nous utilisons false, pour dire que nous n'envoyons pas de données.
            function (data){
                console.log(data);
                if (data['state'] == true){
                    $('#lampedevant').addClass('on');
                    $('#lampedevant').removeClass('off');

                } else {
                    $('#lampedevant').addClass('off');
                    $('#lampedevant').removeClass('on');
                }

            },
            'json' // Format des données reçues.
        );
    },2000);
});
