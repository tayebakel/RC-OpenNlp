from arabicdialect import arabicdialect

 a r _ e g   =   a r a b i c d i a l e c t ( ' e g y p t i a n ' ) 
 n o n _ e g y p t i a n _ t w e e t   ="ما رتبت فوضاك غير الي نفت روحها في واد صمتك للأخير . غير ذي زرع ... ولكنه نبت  صار موطن للشعر حول الغدير  #وجد"
 e g y p t i a n _ t w e e t   = "-حبيبي إيه رأيك في عينيا في الشمس؟ =و الله أنا مش شايف في الشمس غير شنبك."
 p r i n t ( a r _ e g . c l a s s i f y _ o n e ( e g y p t i a n _ t w e e t ) ) 
 p r i n t ( a r _ e g . c l a s s i f y _ o n e ( n o n _ e g y p t i a n _ t w e e t ) ) 
 p r i n t ( a r _ e g . c l a s s i f y _ m a n y ( [ n o n _ e g y p t i a n _ t w e e t , e g y p t i a n _ t w e e t ] ) )