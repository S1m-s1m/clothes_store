# def review_view(request, pk):
#     form = Review_form(request.POST)
#     cloth = Clothes.objects.get(id=pk)
#     if form.is_valid():
#         form = form.save(commit=False)
#         form.cloth = cloth
#         form.save()
#     return redirect('/')

# path('review/<int:pk>/', views.review_view, name='add_review'),

# <div align="center" id="review">
#         <h2 align="center"><strong>Комментирование</strong></h2>
#         <form id="review_form" method="post" action="">
#             {% csrf_token %}
#             {{ form.as_p }}
#             <p><input type="submit" value="отправить"></p>
#         </form>
# <!--        {% for review in cloth.review_set.all %}-->
# <!--            {{ review.name }}-->
# <!--            {{ review.text }}-->
# <!--        {% endfor %}-->
#     </div>

# <table id='main_table_form' border="1" align="center" bgcolor="white" cellpadding="10" cellspacing="30" width="964" bordercolor="black">
#     <caption><strong><h1>Отправка отзыва</h1></strong></caption>
#     <tr><td><form method="post" action="" enctype="multipart/form-data">
#         {% csrf_token %}
#         <p>{{ form.image }}</p>
#         <p>{{ form.name }}</p>
#         <p>{{ form.sex }}</p>
#         <p>{{ form.cost }}</p>
#         <p>{{ form.seasons }}</p>
#         <p>{{ form.url }}</p>
#         <p>{{ form.size }}</p>
#         <p>{{ form.availability }}</p>
#         <span>{{ error }}</span>
#         <p><input type="reset" value="сбросить"></p>
#         <p><input type="submit" value="отправить"></p>
# </form></td></tr>
# </table>

text = "555555555555555555555555555555555555555555555555555555555555555555555555555555"
for i in text:
    res = text.count(i)

print(res)

#8B7AA8
#7AA899