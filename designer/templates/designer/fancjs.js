 $().fancybox({
          selector : '.imglist a:visible',
          thumbs   : {
            autoStart : true
          }
        });

        // Simple filter
        $('#filter').on('change', function() {
          var $visible, val = this.value;

          if (val) {
            $visible = $('.imglist a').hide().filter('.' + val);

          } else {
            $visible = $('.imglist a');
          }

          $visible.show();
        });
