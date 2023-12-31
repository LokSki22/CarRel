# Tugas 2,3,4,5,6 PBP (Tugas 6 diatas, Tugas lainnya dibawah)

# CarRel Application 
# [Link App](https://carrel.adaptable.app/main/)
# **Muhammad Farrel Altaf (2206829332) - PBP B**



# Tugas 6
## **No 1**
1. Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.
* _Synchronous programming_ adalah metode pemrograman di mana operasi atau tugas-tugas dieksekusi secara berurutan. Dalam metode ini, jika ada operasi yang memerlukan durasi panjang, seluruh program akan menunggu dan tidak dapat melaksanakan operasi lain hingga operasi tersebut berakhir.

* _Asynchronous programming_ adalah metode pemrograman  yang memungkinkan operasi untuk berjalan di latar belakang dan tidak menghalangi (blocking) eksekusi operasi lainnya. Dalam metode ini, tugas yang membutuhkan waktu yang lama dapat dijalankan secara bersamaan dengan tugas lainnya, sehingga program dapat terus berjalan tanpa terhenti.

* Dalam pemrograman _Asynchronous programming_, program memanfaatkan fungsi callback atau promise untuk mengatasi hasil dari operasi yang sedang dijalankan. Fungsi callback akan diaktifkan saat operasi selesai, sementara promise memberikan nilai setelah operasi rampung. Sebaliknya, dalam _Synchronous programming_ , program akan menanti hingga sebuah operasi selesai sebelum bergerak ke operasi selanjutnya, jadi tidak diperlukan fungsi callback atau promise.


## **No 2**
2. Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma event-driven programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini. 
* Paradigma event-driven programming merupakan di mana alur eksekusi program ditentukan oleh sejumlah peristiwa, seperti tindakan _user_ (klik mouse, klik keyboard) atau pesan dari program lain atau thread. Contohnya, pada tugas ini, event-driven programming digunakan untuk menangani event yang terjadi pada aplikasi web seperti klik tombol, input teks, dan lain-lain.



## **No 3**
3. Jelaskan penerapan asynchronous programming pada AJAX.
* Dalam AJAX, asynchronous programming memungkinkan kita untuk mengambil informasi dari server tanpa perlu memperbarui seluruh halaman. Dengan _asynchronous programming_, saat permintaan dikirim ke server, eksekusi program lain dapat berlanjut tanpa menunggu balasan dari server. Begitu balasan diterima, program kemudian menjalankan fungsi tertentu untuk memproses informasi tersebut. Pendekatan ini meningkatkan efisiensi dan responsivitas aplikasi web, memberikan pengalaman yang lebih mulus bagi pengguna tanpa perlu menunggu pembaruan halaman penuh.


## **No 4**
4. Pada PBP kali ini, penerapan AJAX dilakukan dengan menggunakan Fetch API daripada library jQuery. Bandingkanlah kedua teknologi tersebut dan tuliskan pendapat kamu teknologi manakah yang lebih baik untuk digunakan
* Sejak munculnya AJAX, library jQuery telah menjadi instrumen utama dalam implementasinya, menawarkan cara sederhana untuk melakukan permintaan asinkron. Keunggulan dari AJAX melalui jQuery terletak pada kompatibilitas lintas browser-nya, memastikan fungsionalitas bahkan pada browser yang lebih tua yang belum mendukung teknologi web terkini. Namun, seiring berjalannya waktu, browser modern telah menawarkan Fetch API yang merupakan fitur bawaan browser modern, memungkinkan permintaan asinkron tanpa kebutuhan library tambahan. Fetch API menyediakan fleksibilitas lebih dalam mengelola permintaan dan respons, dan mendukung teknologi terbaru seperti promises dan async/await. Mengingat Fetch API adalah standar web modern, dukungan lintas browser sudah luas, dan ini menghilangkan kebutuhan library tambahan. 
* Untuk sekarang, Fetch API sering kali dipilih karena kode yang lebih efisien, tidak adanya ketergantungan, dan kapabilitas aslinya. Meskipun demikian, untuk aplikasi yang fokus pada kompatibilitas atau telah mengadopsi jQuery sepenuhnya, AJAX melalui jQuery masih memiliki tempatnya.

## **No 5**
5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
* Mengubah tugas 5 yang dibuat sebelumnya menjadi menggunakan AJAX
  - AJAX GET
    - Ubahlah kode cards data item agar dapat mendukung AJAX GET. 
      
      - Lalu saya mengubah card template agar bisa memanfaatkan script AJAX GET di `main.html`
        ```html
        <div class="center-content">

        ...
  
        <div id="cardContainer"></div>
    
        </div>
        ```
    - Lakukan pengambilan task menggunakan AJAX GET.  
      - Saya membuat fungsi `get_product_json` untuk mendapatkan data item dengan format json per id di `views.py` dengan kode:
        ```python
        def get_product_json(request):
            product_item = Item.objects.all()
            return HttpResponse(serializers.serialize('json', product_item))

        ```
      
      - Saya lakukan routing di `urls.py` 
        ```python
        path('get-product/', get_product_json, name='get_product_json'),
        ```
      
      - Saya tambahkan function javascript di `main.html` :
        ```javascript
        async function getProducts() {
        return fetch("{% url 'main:get_product_json' %}").then((res) => res.json())
        }
        ```
      
      
  - AJAX POST      
    - Buatlah sebuah tombol yang membuka sebuah modal dengan form untuk menambahkan item. 
      - Saya membuat modal serta sebuah tombol untuk menambahkan produk dengan AJAX di `main.html` dengan kode berikut:
        ```html
        <div class="center-content">

        <div class="button-container">
            <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal">Add Product by AJAX</button>
        </div>
    
        ...
    
        </div>
        
        
        <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h1 class="modal-title fs-5" id="exampleModalLabel">Add New Product</h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <form id="form" onsubmit="return false;">
                        {% csrf_token %}
                        <div class="mb-3">
                            <label for="name" class="col-form-label">Name:</label>
                            <input type="text" class="form-control" id="name" name="name"></input>
                        </div>
                        <div class="mb-3">
                            <label for="categories" class="col-form-label">Categories:</label>
                            <textarea class="form-control" id="categories" name="categories"></textarea>
                        </div>
                        <div class="mb-3">
                            <label for="description" class="col-form-label">Description:</label>
                            <textarea class="form-control" id="description" name="description"></textarea>
                        </div>
                        <div class="mb-3">
                            <label for="price" class="col-form-label">Price:</label>
                            <input type="number" class="form-control" id="price" name="price"></input>
                        </div>
                        <div class="mb-3">
                            <label for="amount" class="col-form-label">Amount:</label>
                            <input type="number" class="form-control" id="amount" name="amount"></input>
                        </div>
                    </form>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                    <button type="button" class="btn btn-primary" id="button_add" data-bs-dismiss="modal">Add Product</button>
                </div>
            </div>
        </div>
        </div>

        ```
    - Buatlah fungsi view baru untuk menambahkan item baru ke dalam basis data.
      - Saya membuat fungsi `add_product_ajax` di views.py yang dapat di implementasikan di main.html
        ```python
        def add_product_ajax(request):
        if request.method == 'POST':
        name = request.POST.get("name")
        price = request.POST.get("price")
        amount = request.POST.get("amount")
        description = request.POST.get("description")
        categories = request.POST.get("categories")
        user = request.user

        new_product = Item(name=name, price=price, description=description, user=user, amount=amount, categories=categories)
        new_product.save()

        return HttpResponse(b"CREATED", status=201)
        return HttpResponseNotFound()

        ```
    - Buatlah path /create-ajax/ yang mengarah ke fungsi view yang baru kamu buat. 
      - Lalu saya lakukan routing di `urls.py`
        ```python
        path('create-product-ajax/', add_product_ajax, name='add_product_ajax'),
        ```
    - Hubungkan form yang telah kamu buat di dalam modal kamu ke path /create-ajax/. 
      - Saya membuat function ini di script `main.html`
        ```javascript
        function addProduct() {
        fetch("{% url 'main:add_product_ajax' %}", {
            method: "POST",
            body: new FormData(document.querySelector('#form'))
        }).then(refreshProducts)

        document.getElementById("form").reset()
        return false
        }
        document.getElementById("button_add").onclick = addProduct

        ```
    
    - Lakukan refresh pada halaman utama secara asinkronus untuk menampilkan daftar item terbaru tanpa reload halaman utama secara keseluruhan.
      - Lalu saya membuat script di `main.html` agar page selalu refresh dengan menampilkan data terbaru
        ```javascript
        async function refreshProducts() {
        const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
        const container = document.getElementById("cardContainer");
        container.innerHTML = "";  // Clear the current content.
    
        const products = await getProducts();
    
        products.forEach((item, index) => {
            container.innerHTML += `
                <div class="col-12 mb-3" style="padding-left: 100px; padding-right: 100px;"> <!-- Adjusted grid class and added inline styles for margins -->
                    <div class="card ${index === products.length - 1 ? 'bg-clr' : ''}">
                        <div class="card-body" style="position: relative;">
                            <h5 class="card-title">${item.fields.name}</h5>
                            <p class="card-text">Categories: ${item.fields.categories}</p>
                            <p class="card-text">Description: ${item.fields.description}</p>
                            <p class="card-text"><strong>Price: ${item.fields.price}</strong></p>
                            <p class="card-text">Date Added: ${item.fields.date_added}</p>
    
                            <form method="post">
                                <input type="hidden" name="csrfmiddlewaretoken" value="${csrfToken}">
                                <div style="display: flex; flex-direction: column; justify-content: flex-start;">
                                    <div style="display: flex; align-items: center;">
                                        <button
                                                onclick="incrementProduct(event, ${item.pk})"
                                                style="border: none;">
                                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-plus" viewBox="0 0 16 16">
                                                <path d="M8 4a.5.5 0 0 1 .5.5v3h3a.5.5 0 0 1 0 1h-3v3a.5.5 0 0 1-1 0v-3h-3a.5.5 0 0 1 0-1h3v-3A.5.5 0 0 1 8 4z"></path>
                                            </svg>
                                        </button>
                                        <p class="card-text" style="margin: 0 10px;">Amount: ${item.fields.amount}</p>
                                        <button
                                                onclick="decrementProduct(event, ${item.pk})"
                                                style="border: none;">
                                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-dash" viewBox="0 0 16 16">
                                                <path d="M4 8a.5.5 0 0 1 .5-.5h7a.5.5 0 0 1 0 1h-7A.5.5 0 0 1 4 8z"></path>
                                            </svg>
                                        </button>
                                    </div>
    
                                    <button type="button"
                                            onclick="deleteProduct(${item.pk})"
                                            style="position: absolute; top: 10px; right: 10px; background: none; border: none; ">
                                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-trash" viewBox="0 0 16 16">
                                            <path d="M5.5 5.5A.5.5 0 0 1 6 6v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5Zm2.5 0a.5.5 0 0 1 .5.5v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5Zm3 .5a.5.5 0 0 0-1 0v6a.5.5 0 0 0 1 0V6Z"></path>
                                            <path d="M14.5 3a1 1 0 0 1-1 1H13v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V4h-.5a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1H6a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1h3.5a1 1 0 0 1 1 1v1ZM4.118 4 4 4.059V13a1 1 0 0 0 1 1h6a1 1 0 0 0 1-1V4.059L11.882 4H4.118ZM2.5 3h11V2h-11v1Z"></path>
                                        </svg>
                                    </button>
    
    
                                </div>
                            </form>
                        </div>
                    </div>
                </div>`;
        });
         updateItemsTotal(products.length);
        }
    
        refreshProducts();
        ```
      - Saya menambahkan fungsi increment dan decrement produk dengan ajax. 
        ```javascript
        function incrementProduct(event, id) {
        event.preventDefault();
        fetch("/increment-item-ajax/" + id + "/", {
            method: "POST"
        }).then(refreshProducts)
        }
    
        function decrementProduct(event, id) {
            event.preventDefault();
            fetch("/decrement-item-ajax/" + id + "/", {
                method: "POST"
            }).then(refreshProducts)
        }
        ```
        Mereka dipanggil dengan `onclick="incrementProduct(event, ${item.pk})"` dan ` onclick="decrementProduct(event, ${item.pk})"`


  - Melakukan perintah collectstatic
    - Pada settings.py, tambahkan `STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')` di bawah STATIC_URL.
    - Jalankan perintah python manage.py collectstatic untuk mengumpulkan semua file static ke folder staticfiles.
    
## **No 6**
* BONUS tugas 6
  - Menambahkan fungsionalitas hapus dengan menggunakan AJAX DELETE
    - Saya membuat fungsi `delete_item_ajax` pada `views.py`
      ```python
        def delete_item_ajax(request, id):
            item = Item.objects.get(pk=id)
            item.delete()
            return HttpResponse(b"DELETED", status=201)
      ```
    - Lakukan routing pada `urls.py`
      ```python
        path('delete-item-ajax/<int:id>/', delete_item_ajax, name='delete_item_ajax'),
      ```
    - Menambahkan function berukut di main.html
      ```javascript
        function deleteProduct(id) {
        fetch("/delete-item-ajax/" + id + "/", {
            method: "POST"
        }).then(refreshProducts)
    
        document.getElementById("form").reset()
        return false
        }
      ```
    - Mencantumkan function script `deleteProduct` di button delete
      ```javascript
        <button type="button"
           onclick="deleteProduct(${item.pk})" ->Scriptnya
           style="position: absolute; top: 10px; right: 10px; background: none; border: none; ">
          <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-trash" viewBox="0 0 16 16">
                <path d="M5.5 5.5A.5.5 0 0 1 6 6v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5Zm2.5 0a.5.5 0 0 1 .5.5v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5Zm3 .5a.5.5 0 0 0-1 0v6a.5.5 0 0 0 1 0V6Z"></path>
                <path d="M14.5 3a1 1 0 0 1-1 1H13v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V4h-.5a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1H6a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1h3.5a1 1 0 0 1 1 1v1ZM4.118 4 4 4.059V13a1 1 0 0 0 1 1h6a1 1 0 0 0 1-1V4.059L11.882 4H4.118ZM2.5 3h11V2h-11v1Z"></path>
          </svg>
        </button>
      ```

# Tugas 5
## **No 1**
1. Jelaskan manfaat dari setiap element selector dan kapan waktu yang tepat untuk menggunakannya.
* _Element Selector_
    - Selector Elemen digunakan untuk mengubah _style_ properti untuk semua elemen properti yang memiliki tag HTML yang sama.
    - Contohnya sebagai berikut:
      - ```html
        <body>
          <div>
            <h1>Test 1</h1>
            <h2>Test 2</h2>
          </div>
          ...
        </body>
        ```    
        Lalu kita dapat menggunakan element sebagai selector dalam CSS. Formatnya _[id_name]_ (tanpa menggunakan simbol)
      - ```html
        h1 {
          color: #fca205;
          font-family: "Poppins";
          font-style: italic;
        }
        ```
* _ID Selector_
    - ID Selector menggunakan ID pada tag untuk menjadi selector-nya. Sebuah ID bersifat unik dalam satu halaman web
    - Contoh penggunaanya:
      ```html
        <body>
          <div id="header"> 
            <h1>Test Hi!</h1>
          </div>
         ...
        </body>
      ```
      Setelah itu, kita dapat menggunakan id sebagai selector dalam file CSS. Formatnya #[id_name]. Cocok untuk menargetkan elemen yang spesifik
      ```html
        #header {
         background-color: #f0f0f0;
         margin-top: 0;
         padding: 20px 20px 20px 40px;
       }
      ```

* _Class Selector_
    - _Class Selector_ dapat memungkinkan kita mengelompokkan lebih dari satu elemen dengan karakteristik yang sama.
    - Contoh:
      ```html
       <div id="main">
        <div class="content_section">
            <p class="date">published: 28 September 2022</p>
            <h2><a href="">Tutorial CSS ku</a></h2>
            <p id="content_1">Yay ini tutorial yang gampang!</p>
        </div>
        <div class="content_section">
            <p class="date ">published: 29 September 2022</p>
            <h2><a href="">Tutorial CSS mu</a></h2>
            <p id="content_2">Yay ini tutorial yang mudah!</p>
        </div>
        <div class="content_section">
            <p>published: 30 September 2022</p>
            <h2><a href="">Tutorial CSS semua</a></h2>
            <p id="content_3">Yay ini tutorial yang tidak sulit!</p>
        </div>
       </div>
      ```
      Setelah itu kita dapat menggunakan class tersebut sebagai selector di file CSS. Formatnya ._[class_name]_
      ```html
       .content_section {
         background-color: #3696e1;
         margin-bottom: 30px;
         color: #000000;
         font-family: cursive;
        padding: 20px 20px 20px 40px;
       } 
      ```        



## **No 2**
2. Jelaskan HTML5 Tag yang kamu ketahui.
* | No | Tag           |Penjelasan |
   |----|---------------|---|
   | 1  | `<html>`      |  digunakan untuk mengawali dan mengakhiri seluruh kode atau dokumen HTML
   | 2  | `<head>`      |  digunakan untuk menyertakan informasi meta, judul halaman web, dan menghubungkan html dengan _stylesheet_ serta Javascript
   | 3  | `<title>`     |  digunakan untuk menentukan judul halaman web yang ditampilkan
   | 4  | `<meta>`      |  digunakan untuk mendefinisikan metadata tentang halaman web, seperti karakter set, deskripsi, dan informasi lain yang relevan.
   | 5  | `<link>`      |  digunakan untuk mengawali dan mengakhiri seluruh kode atau dokumen HTML
    | 6  | `<body>`      |   berisi konten utama halaman web yang akan ditampilkan kepada pengguna, seperti teks, gambar, dan elemen-elemen lainnya.
   | 7  | `<h1> - <h6>` |  Tag-tag ini digunakan untuk mengatur tingkat judul atau heading. h1 adalah yang tertinggi , sementara h6 adalah yang terendah.HTML
   | 8  | `<p>`         |  digunakan untuk membuat paragraf teks.
   | 9  | `<a>`         |  digunakan untuk membuat tautan atau hyperlink ke halaman web atau sumber daya lainnya.
   | 10 | `<img>`      |  digunakan untuk menampilkan gambar di halaman web.
   | 11 | `<ul>`      |  digunakan untuk membuat daftar tak terurut (unordered list), yang berisi elemen-elemen dalam bentuk daftar bulleted.
   | 12 | `<ol>`      |  digunakan untuk membuat daftar terurut (ordered list), yang berisi elemen-elemen dalam bentuk daftar bernomor.
   | 13 | `<li>`      |  digunakan untuk mendefinisikan elemen-elemen dalam daftar (baik daftar tak terurut maupun terurut).
   | 14 | `<div>`      |  elemen blok yang digunakan untuk mengelompokkan dan mengatur elemen-elemen HTML lainnya dalam sebuah kotak atau wadah. Ini sering digunakan dalam desain tata letak halaman.
   | 15 | `<span>`      |  digunakan untuk mengaplikasikan gaya atau mengelompokkan sebagian kecil dari teks atau elemen dalam dokumen.
 

## **No 3**
3. Jelaskan perbedaan antara margin dan padding.
* | Perbedaan | Margin   | Padding                                                       |
   |-----------|----------|---------------------------------------------------------------|
   | Fungsi Utama         | Ruang di luar elemen, mempengaruhi tata letak elemen dalam hubungannya dengan elemen lain di sekitarnya. | Ruang di dalam elemen, mempengaruhi tampilan dan tata letak konten elemen.
   | Dampak pada Ukuran       | Margin dapat memengaruhi ukuran keseluruhan elemen, membuatnya terlihat lebih besar dan memiliki ruang kosong di sekitarnya. | Padding tidak memengaruhi ukuran keseluruhan elemen; ukuran elemen tetap sama, hanya kontennya yang terdorong ke dalam.
   | Pengaruh terhadap Konten         | Tidak ada pengaruh langsung terhadap konten elemen. | Memengaruhi tampilan dan tata letak konten dalam elemen.
   | Tampilan Visual       | Tampilan visual dari margin adalah ruang kosong di sekitar elemen yang ditentukan oleh warna latar belakang elemen lain di sekitarnya | Tampilan visual dari padding adalah ruang kosong di sekitar konten elemen, yang ditentukan oleh warna latar belakang elemen itu sendiri.
   | Pengaruh terhadap Konten         | Margin dapat digunakan dengan elemen blok maupun inline. | Padding biasanya digunakan dengan elemen blok; elemen inline memiliki padding horizontal tetapi tidak memiliki padding vertikal.


## **No 4**
4. Jelaskan perbedaan antara framework CSS Tailwind dan Bootstrap. Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya?
* | Perbedaan    | Tailwind CSS                                                                                                                    | Bootstrap                                                                                                                                |
   |--------------|---------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
   | Desain       | Utility-first" dan fleksibel.                        | Desain lebih terstruktur dan kaku.                                                             
   | Ukuran File  | Lebih kecil karena hanya mengandalkan kelas-kelas utilitas yang digunakan.    | Lebih besar karena sudah mencakup banyak komponen dan gaya desain.                  
   | Kustomisasi  | Tingkat kustomisasi yang tinggi, Anda dapat mengontrol setiap aspek desain.                                                                             | Kustomisasi mungkin tidak sefleksibel karena Bootstrap memiliki desain yang sudah ditentukan.                                                                                 
   | Kecepatan    | Memerlukan waktu lebih lama untuk menggabungkan kelas-kelas utilitas. | Lebih cepat membangun situs dengan komponen siap pakai.
   | Jenis Proyek | Cocok untuk proyek yang membutuhkan desain unik dan tingkat kustomisasi yang tinggi                                                                     | Cocok untuk proyek yang membutuhkan pembangunan cepat dengan desain yang sudah ada.         



## **No 5**
5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
* Kustomisasi desain pada templat HTML yang telah dibuat pada Tugas 4 dengan menggunakan CSS atau CSS framework (seperti Bootstrap, Tailwind, Bulma) dengan ketentuan sebagai berikut
  - Saya menambahkan link CSS framework dalam `templates/base.html`. Saya memakai bootstrap pada tugas 5 ini
  ```html
    {% load static %}
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="UTF-8" />
            <meta
                name="viewport"
                content="width=device-width, initial-scale=1.0"
            />
            {% block meta %}
            {% endblock meta %}
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
            <script src="https://code.jquery.com/jquery-3.6.0.min.js" integrity="sha384-KyZXEAg3QhqLMpG8r+J4jsl5c9zdLKaUk5Ae5f5b1bw6AUn5f5v8FZJoMxm6f5cH1" crossorigin="anonymous"></script>
            <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.8/dist/umd/popper.min.js" integrity="sha384-I7E8VVD/ismYTF4hNIPjVp/Zjvgyol6VFvRkX/vR+Vc4jQkC+hVqc2pM8ODewa9r" crossorigin="anonymous"></script>
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.min.js" integrity="sha384-BBtl+eGJRgqQAUMxJ7pMwbEyER4l1g+O15P+16Ep7Q9Q+zqX6gSbd85u4mG4QzX+" crossorigin="anonymous"></script>
        </head>

    <body>
        {% block content %}
        {% endblock content %}
    </body>
    </html>
  ```
  
  - Saya menambahkan fitur edit untuk tugas 5, untuk fitur delete saya sudah menambahkan saat tugas 4
  ```python
  def edit_item(request, id):
    # Get product berdasarkan ID
    item = Item.objects.get(pk = id)

    # Set product sebagai instance dari form
    form = ItemForm(request.POST or None, instance=item)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_item.html", context)
  ```
  Saya menambahkan fitur `edit_item` pada `views.py` subdirektori main. Setelah itu saya membuat file html `edit_item.html` dengan isi kode sebagai berikut:
  ```python
   {% extends 'base.html' %}

    {% load static %}
    
    {% block content %}
    <div class="container">
        <div class="row justify-content-center">
            <div class="col-md-8">
                <div class="card">
                    <div class="card-header">Edit Item</div>
                    <div class="card-body">
                        <form method="POST">
                            {% csrf_token %}
                            <table class="table">
                                {{ form.as_table }}
                                <tr>
                                    <td></td>
                                    <td>
                                        <button type="submit" class="btn btn-primary">Edit Product</button>
                                    </td>
                                </tr>
                            </table>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </div>
    {% endblock %}

  ```
  Setelah itu saya melakukan import fungsi tersebut di `urls.py` subdirektori main dan melakukan _routing_ dengan kode sebagai berikut:
  ```python
  from django.urls import path
    from main.views import show_main, create_item, show_xml, show_json, show_xml_by_id, show_json_by_id
    from main.views import register #sesuaikan dengan nama fungsi yang dibuat
    from main.views import login_user #sesuaikan dengan nama fungsi yang dibuat
    from main.views import logout_user
    from main.views import edit_item #import disini
    app_name = 'main'
    
    
    urlpatterns = [
        path('', show_main, name='show_main'),
        path('create-item', create_item, name='create_item'),
        path('xml/', show_xml, name='show_xml'),
        path('json/', show_json, name='show_json'),
        path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
        path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
        path('register/', register, name='register'),
        path('login/', login_user, name='login'),
        path('logout/', logout_user, name='logout'),
        path('edit-item/<int:id>', edit_item, name='edit_item'), #routing disini
    
    ]

  ```
  - Lalu saya panggil edit item di `main.html` dengan potongan kode sebagai berikut
  ```html
  <a href="{% url 'main:edit_item' item.pk %}" class="edit-button">
      Edit
  </a>
  ```
* Kustomisasi halaman login, register, dan tambah inventori semenarik mungkin.
  - Pada halaman login, saya memakai bootstrap untuk memperbarui tampilan halaman login saya. Saya memanfaatkan container `card` untuk menampilkan form login
  ```html
   {% extends 'base.html' %}

    {% block meta %}
        <title>Login</title>
    {% endblock meta %}
    
    {% block content %}
    <style>
    body {
        font-family: 'General Sans', sans-serif;
    }
    </style>
    <div class="container">
        <div class="card mx-auto mt-5" style="max-width: 400px;">
            <div class="card-body">
                <h1 class="card-title">Login</h1>
                <form method="POST" action="">
                    {% csrf_token %}
                    <div class="mb-3">
                        <label for="username" class="form-label">Username:</label>
                        <input type="text" name="username" id="username" class="form-control" placeholder="Username">
                    </div>
                    <div class="mb-3">
                        <label for="password" class="form-label">Password:</label>
                        <input type="password" name="password" id="password" class="form-control" placeholder="Password">
                    </div>
                    <button type="submit" class="btn btn-primary">Login</button>
                </form>
                {% if messages %}
                    <ul class="mt-3">
                        {% for message in messages %}
                            <li>{{ message }}</li>
                        {% endfor %}
                    </ul>
                {% endif %}
                <p class="mt-3">Don't have an account yet? <a href="{% url 'main:register' %}">Register Now</a></p>
            </div>
        </div>
    </div>
    {% endblock content %}
  ```
  - Pada halaman register, saya juga memakai bootstrap dan menggunakan container `card` 
  ```html
   {% extends 'base.html' %}

    {% block meta %}
        <title>Register</title>
    {% endblock meta %}
    
    {% block content %}  
    <style>
    body {
        font-family: 'General Sans', sans-serif;
    }
    </style>
    <div class="container mt-5">
        <div class="row justify-content-center">
            <div class="col-md-6">
                <div class="card">
                    <div class="card-body">
                        <h1 class="card-title">Register</h1>
                        <form method="POST">
                            {% csrf_token %}
                            {{ form.as_table }}
                            <div class="text-center">
                                <button type="submit" class="btn btn-primary">Daftar</button>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </div>
    {% endblock content %}
  ```
* Pada halaman main, saya juga memakai bootstrap untuk memperbarui tampilan halaman main. Di halaman main, saya dapat menambahkan item, meng-delete, menambahkan jumlah item tertentu, dan meng-edit item tertentu.
  ```html
  {% extends 'base.html' %}

    {% block content %}
    <style>
        body {
            font-family: 'General Sans', sans-serif;
        }
    
        /* Style for the card title */
        .card-title {
            font-family: 'General Sans', sans-serif;
        }
    
        /* Style for the CarRel text in the navbar */
        .navbar-brand {
            font-weight: bold;
        }
    
        /* Style for the Logout button */
        .btn-logout {
            background-color: red;
            color: white;
        }
    
        /* Add left and right padding to the container */
        .container-padded {
            padding-left: 80px;
            padding-right: 80px;
        }
    
        /* Center-align all items */
        .center-align {
            text-align: center;
        }
    
        btn-floating {
            position: fixed;
            bottom: 20px; /* Jarak dari bawah */
            right: 20px; /* Jarak dari kanan */
            z-index: 1000; /* Untuk mengatasi tumpukan elemen lain */
        }
    
        .edit-button {
              margin-top: 10px;
              display: inline-flex;
              height: 48px;
              padding: 4px 16px;
              justify-content: center;
              align-items: center;
              gap: 8px;
              border-radius: 6px;
              background: blueviolet;
              color: #fff;
              text-decoration: none;
              border: none;
              cursor: pointer;
          }
    
        .btn-add {
            margin-bottom: 10px;
        }
    
        .bg-clr {
            background-color: bisque;
        }
    
    </style>
    
    <nav class="navbar navbar-expand-lg bg-body-tertiary">
        <div class="container-fluid">
            <a class="navbar-brand" href="#">CarRel's Shop</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <ul class="navbar-nav me-auto">
                    <li class="nav-item">
                    </li>
                </ul>
                <a href="{% url 'main:logout' %}">
                    <button class="btn btn-logout btn-outline-danger" type="button">Logout</button>
                </a>
            </div>
        </div>
    </nav>
    
    <p class="center-align" style="font-size: 120%;">
        Selamat datang <strong>{{ name }}</strong> dari kelas <strong>{{ class }}</strong> !
    </p>
    
    <p class="center-align" style="font-size: 100%;">
        Anda menyimpan <strong>{{ item_count }} jenis mobil</strong> pada aplikasi CarRel
    </p>
    
    </p>
    
    
    <div class="container" >
    
        <div class="row">
        <a href="{% url 'main:create_item' %}" class="center-align btn-add">
                <button class="btn btn-primary btn-add">Add New Item</button>
        </a>
            {% for item in items%}
                <div class="col-md-4 mb-3">
                    <div class="card {% if forloop.last %}bg-clr{% endif %}">
                        <div class="card-body" style="position: relative;">
                            <h5 class="card-title">{{ item.name }}</h5>
                            <p class="card-text">Categories: {{ item.categories }}</p>
                            <p class="card-text">Description: {{ item.description }}</p>
                            <p class="card-text"><strong>Price: {{ item.price }}</strong></p>
                            <p class="card-text">Date Added: {{ item.date_added }}</p>
    
    
                            <form method="post">
    
                                {% csrf_token %}
                                <div style="display: flex; flex-direction: column; justify-content: flex-start;">
                                    <div style="display: flex; align-items: center;">
                                        <button type="submit" name="increment" value="{{ item.id }}" style="border: none;">
                                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-plus" viewBox="0 0 16 16">
                                                <path d="M8 4a.5.5 0 0 1 .5.5v3h3a.5.5 0 0 1 0 1h-3v3a.5.5 0 0 1-1 0v-3h-3a.5.5 0 0 1 0-1h3v-3A.5.5 0 0 1 8 4z"></path>
                                            </svg>
                                        </button>
                                        <p class="card-text" style="margin: 0 10px;">Amount: {{ item.amount }}</p>
                                        <button type="submit" name="decrement" value="{{ item.id }}" style="border: none;">
                                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-dash" viewBox="0 0 16 16">
                                                <path d="M4 8a.5.5 0 0 1 .5-.5h7a.5.5 0 0 1 0 1h-7A.5.5 0 0 1 4 8z"></path>
                                            </svg>
                                        </button>
                                    </div>
                                    <button type="submit" name="delete" value="{{ item.id }}" style="position: absolute; top: 10px; right: 10px; background: none; border: none;">
                                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-trash" viewBox="0 0 16 16">
                                        <path d="M5.5 5.5A.5.5 0 0 1 6 6v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5Zm2.5 0a.5.5 0 0 1 .5.5v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5Zm3 .5a.5.5 0 0 0-1 0v6a.5.5 0 0 0 1 0V6Z"></path>
                                        <path d="M14.5 3a1 1 0 0 1-1 1H13v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V4h-.5a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1H6a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1h3.5a1 1 0 0 1 1 1v1ZM4.118 4 4 4.059V13a1 1 0 0 0 1 1h6a1 1 0 0 0 1-1V4.059L11.882 4H4.118ZM2.5 3h11V2h-11v1Z"></path>
                                        </svg>
                                    </button>
                                     <a href="{% url 'main:edit_item' item.pk %}" class="edit-button">
                                        Edit
                                     </a>
                                </div>
                            </form>
    
                        </div>
                    </div>
                </div>
            {% endfor %}
        </div>
    </div>

    <h5 class="center-align" style="margin-top: 20px;">Sesi terakhir login: {{ last_login }}</h5>
    {% endblock content %}
    ```h

## **No Bonus**
* Saya memberikan warna card yang berbeda pada item yang terakhir kali ditambahkan dengan potongan kode sebagai berikut:
  ```html
   {% for item in items%}
            ...
                <div class="card {% if forloop.last %}bg-clr{% endif %}"> 
  ```
  Pada loop yang menampilkan seluruh item yang ditambahkan, item yang terakhir kali ditampilkan akan memiliki style backgorund tersendiri.
* Berikut screenshot tampilannya:
![img_5.png](img_5.png)

# Tugas 4
## **No 1**
1. Apa itu Django `UserCreationForm`, dan jelaskan apa kelebihan dan kekurangannya?
* UserCreationForm adalah sebuah kelas formulir yang disediakan oleh Django, sebuah framework _web development_ berbasis Python, untuk menangani proses pembuatan akun pengguna baru.
  Formulir ini merupakan bagian dari modul django.contrib.auth.forms dan secara default mencakup validasi untuk kolom username, password1, dan password2. 
* Kelebihan :
  - Mudah diintegrasikan karena merupakan bagian dari framework Django.
  - Memiliki fitur validasi otomatis seperti seperti memastikan kata sandi memenuhi kriteria tertentu dan `username` unik.
  - Dapat dikustomisasi sesuai kebutuhan.
  - Memiliki keamanan yang baik.
* Kekurangan :
  - Fitur yang terbatas jika ingin autentikasi dua faktor dan konfirmasi melalui email.
  - Memiliki batasan validasi data yang spesifik.
  - Tampilan yang _default_ dan kurang menarik.

## **No 2**
2. Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?
* Autentikasi
  - Dalam konteks Django, autentikasi adalah proses verifikasi identitas pengguna. Django menyediakan mekanisme autentikasi yang melibatkan penggunaan `username` dan `password`
* Otorisasi
  - Setelah autentikasi, langkah selanjutnya adalah otorisasi, yaitu menentukan apa yang bisa diakses atau dilakukan oleh pengguna yang sudah terautentikasi.
* Mengapa keduanya penting?
  - Penting untuk keamanan.  Tanpa autentikasi dan otorisasi, aplikasi menjadi rentan terhadap serangan dan penyalahgunaan data.
  - Penting untuk kontrol akses. Otorisasi membantu dalam mengatur apa yang boleh dan tidak boleh diakses oleh pengguna.

## **No 3**
3. Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?
* Cookies dalam aplikasi web
  - Cookies adalah file kecil data yang disimpan oleh peramban web di sisi klien. Tujuannya adalah untuk menyimpan informasi tentang sesi pengguna atau preferensi lainnya untuk mempermudah interaksi antara pengguna dan situs web. 
  - Dalam konteks aplikasi web, cookies digunakan untuk mengelola data sesi pengguna, yaitu informasi yang disimpan oleh server tentang pengguna selama mereka menggunakan aplikasi web.
* Bagaimana Django menggunakan cookies
  - Django menggunakan cookies terutama untuk mengelola data sesi pengguna. Ketika pengguna pertama kali mengakses aplikasi web Django, sebuah cookie unik, biasanya dengan nama `sessionid`, dibuat dan disimpan di peramban pengguna. Setiap kali pengguna kembali mengakses aplikasi, cookie ini dikirimkan kembali ke server, yang memungkinkan Django untuk mengidentifikasi dan mengembalikan data sesi yang berhubungan.

## **No 4**
4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?
* Penggunaan cookies dalam pengembangan web tidak bisa dianggap aman secara _default_ dan memerlukan pertimbangan keamanan yang serius. Cookies digunakan untuk menyimpan informasi tentang sesi pengguna, preferensi, atau bahkan kredensial login, dan secara _default_ mereka rentan terhadap sejumlah potensi risiko keamanan.
* Beberapa risiko potensial yang kemungkinan terjadi :
  - Cross-Site Scripting (XSS)
  - Cross-Site Request Forgery (CSRF)
  - Third-Party Cookies
* Tindakan keamanan yang dapat dilakukan untuk mencegah risiko potensial :
  - Mengenkripsi data cookies
  - Menetapkan waktu kadaluarsa dengan tepat
  - Memastikan cookies digunakan pada koneksi yang aman
* Dengan demikian, penting sekali untuk memastikan implementasi cookies yang tepat dan merancang protokol keamanan yang akan melindungi data pengguna yang sensitif. 


## **No 5**
5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step
   * A. Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar.
     - Fungsi Registrasi
       - Saya melakukan import kode berikut di `views.py` pada driketori aplikasi `main`
         ```py
         from django.shortcuts import redirect
         from django.contrib.auth.forms import UserCreationForm
         from django.contrib import messages  
         ```
       - Setelah itu, saya membuat fungsi `register` yang berfungsi untuk meminta parameter request dan diisi dengan kode berikut
         ```py
         def register(request):
         form = UserCreationForm()
    
         if request.method == "POST":
             form = UserCreationForm(request.POST)
             if form.is_valid():
                 form.save()
                 messages.success(request, 'Your account has been successfully created!')
                 return redirect('main:login')
         context = {'form':form}
         return render(request, 'register.html', context)
         ```
       - Lalu saya membuat file `register.html` pada direktori `templates` pada direktori aplikasi main dengan kode sebagai berikut
         ```py
            {% extends 'base.html' %}

            {% block meta %}
                <title>Register</title>
            {% endblock meta %}
            
            {% block content %}  
            
            <div class = "login">
                
                <h1>Register</h1>  
            
                    <form method="POST" >  
                        {% csrf_token %}  
                        <table>  
                            {{ form.as_table }}  
                            <tr>  
                                <td></td>
                                <td><input type="submit" name="submit" value="Daftar"/></td>  
                            </tr>  
                        </table>  
                    </form>
            
                {% if messages %}  
                    <ul>   
                        {% for message in messages %}  
                            <li>{{ message }}</li>  
                            {% endfor %}  
                    </ul>   
                {% endif %}
            
            </div>  
            
            {% endblock content %}
         ```
        - Setelah itu, saya melakukan import fungsi register yang sudah saya buat pada subdirektori `main` 
          ```py
          from main.views import register 
          ``` 
        - Setelah itu, saya menambahkan _path url_ ke dalam `urlpatterns` agar mengakses fungsi register yang sudah syaa buat
          ```py
          path('register/', register, name='register'),
          ```
     
     - Fungsi Login
       - Saya melakukan import kode berikut di `views.py` pada direktori aplikasi main
         ```py
         from django.contrib.auth import authenticate, login        
         ```
       - Kemudian saya membuat fungsi `login_user` di `views.py` pada direktori aplikasi main dengan kode berikut:
         ```py
         def login_user(request):
         if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                response = HttpResponseRedirect(reverse("main:show_main")) 
                response.set_cookie('last_login', str(datetime.datetime.now()))
                return response
            else:
                messages.info(request, 'Sorry, incorrect username or password. Please try again.')
         context = {}
         return render(request, 'login.html', context)
         ```
         Saya memanfaatkan cookie dengan menambahkan `response.set_cookie('last_login', str(datetime.datetime.now()))` dengan key last_login dan value tanggal login pada saat itu
       
        - Setelah itu, saya membuat `login.html` pada direktori `templates` dengan kode berikut:
         ```py
         {% extends 'base.html' %}

         {% block meta %}
             <title>Login</title>
         {% endblock meta %}
            
         {% block content %}
            
         <div class = "login">
            
             <h1>Login</h1>
            
             <form method="POST" action="">
                 {% csrf_token %}
                 <table>
                     <tr>
                         <td>Username: </td>
                         <td><input type="text" name="username" placeholder="Username" class="form-control"></td>
                     </tr>
                                
                     <tr>
                         <td>Password: </td>
                         <td><input type="password" name="password" placeholder="Password" class="form-control"></td>
                     </tr>
            
                     <tr>
                         <td></td>
                         <td><input class="btn login_btn" type="submit" value="Login"></td>
                     </tr>
                 </table>
             </form>
            
             {% if messages %}
                 <ul>
                     {% for message in messages %}
                         <li>{{ message }}</li>
                     {% endfor %}
                 </ul>
             {% endif %}     
                    
             Don't have an account yet? <a href="{% url 'main:register' %}">Register Now</a>
            
         </div>
            
         {% endblock content %}
            
         ```

        - Setelah itu, saya melakukan import pada urls.py pada subdirektori `main` dengan kode berikut:
         ```py
         from main.views import login_user
         ```
        - Setelah itu, saya menambahkan path url untuk login pada `urlpatterns` dengan kode sebagai berikut:
         ```py
         path('login/', login_user, name='login'),
         ```
     - Fungsi Logout
       - Saya melakukan import kode berikut di `views.py` direktori aplikasi
         ```py
         from django.contrib.auth import logout
         ```
       - Setelah itu, saya membuat fungsi `logout_user` di `views.py` direktori aplikasi dengan kode berikut:
         ```py
         def logout_user(request):
           logout(request)
           response = HttpResponseRedirect(reverse('main:login'))
           response.delete_cookie('last_login')
           return response
         ```
         Disini dilakukan penghapusan cookie dengan key `last_login` saat user logout

       - Setelah itu, saya menambahkan button logout di `main.html` dengan kode berikut
         ```py
         
            <a href="{% url 'main:logout' %}">
                <button>
                    Logout
                </button>
            </a>
            
         ```
       - Setelah itu, saya melakukan import fungsi `logout_user` di `urls.py` di subdirektori main
         ```py
         from main.views import logout_user
         ```
       - Setalah itu, saya melakukan routing ke dalam `urlpatterns` di `urls.py` di subdirektori main
         ```py
            path('logout/', logout_user, name='logout'),
         ```
     - Restriksi akses aplikasi
       - import `login_required` di `views.py`
       - Tambahkan `@login_required(login_url='/login')` di atas fungsi `show_main`
   


   * B. Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal.
   ![img_3.png](img_3.png) 
   ![img_2.png](img_2.png)
   

   * C.Menghubungkan model Item dengan User 
     - Melakukan import pada `models.py`
     ```py
     from django.contrib.auth.models import User
     ```
     - Tambahkan potongan kode berikut pada model `Item`
     ```py
     class Item(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE)
     ```
     - Tambahkan potongan kode pada `create_item` di `views.py` agar item yang dibuat terasosiasi pada user
     ```py
     def create_item(request):
         form = ItemForm(request.POST or None)
        
         if form.is_valid() and request.method == "POST":
             item = form.save(commit=False)
             item.user = request.user
             item.save()
             return HttpResponseRedirect(reverse('main:show_main'))
     ```
     - Setelah itu, ubah fungsi `show_main` menjadi
     - ```py
       def show_main(request):
            items = Item.objects.filter(user=request.user)
       ...
        context = {
            'name': request.user.username,
       ...
       ```
     - Setelah itu, jangan lupa lakukan migrasi
   
    
   * D. Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi.  
     - Menampilkan username pengguna
       Pada fungsi `show_main` di `views.py` ubah isi context dengan key `name` menjadi berikut
       ```py
       'name': request.user.username,
       ```
     - Menerapkan cookies last login
       Penerapannya sudah dijelaskan diatas untuk menampilkan last login, lalu tambahkan kode berikut pada context di `show_main`
       ```py
       'last_login': request.COOKIES['last_login'],
       ```
     - Tambahkan kode berikut di `main.html`
       ```py
       <h5>Last login session: {{ last_login }}</h5>
       ```
     - Tampilan 
       ![img_4.png](img_4.png)

## **No 6**
6. Bonus
   - Saya membuat tiga tombol yaitu + Amount (untuk increment amount) , - Amount (untuk decrement amount, dimana batasannya jika amount = 1 maka item tidak bisa dikurangi), dan Delete (delete item) dengan request method POST
   - Pada views.py saya menambahkan kode berikut di `show_main`
   ```py
     def show_main(request):
      items = Item.objects.filter(user=request.user)
      if request.method == 'POST':
          if 'increment' in request.POST:
              item_id = request.POST.get('increment')
              item = items.get(id=item_id)
              item.amount += 1
              item.save()
              return HttpResponseRedirect(reverse('main:show_main'))
          elif 'decrement' in request.POST:
              item_id = request.POST.get('decrement')
              item = items.get(id=item_id)
              if item.amount == 1:
                  item.amount -= 0
              else:
                  item.amount -= 1
              item.save()
              return HttpResponseRedirect(reverse('main:show_main'))
          elif 'delete' in request.POST:
              item_id = request.POST.get('delete')
              item = items.get(id=item_id)
              item.delete()
              return HttpResponseRedirect(reverse('main:show_main'))
     ```
   - Kemudian saya mengubah  `main.html`  bagian table menjadi seperti ini
     ```py
     <table border="1">
        <tr>
            <th>Name</th>
            <th>Categorie</th>
            <th>Description</th>
            <th>Price</th>
            <th>Amount</th>
            <th>Date Added</th>
            <th>Action</th>
        </tr>

        {% comment %} Berikut cara memperlihatkan data produk di bawah baris ini {% endcomment %}

        {% for item in items %}
            <tr>
                <td style="padding: 5px;">{{ item.name }}</td>
                <td style="padding: 5px;">{{ item.categories }}</td>
                <td style="padding: 5px;">{{ item.description }}</td>
                <td style="padding: 5px;">{{ item.price }}</td>
                <td style="padding: 5px;">{{ item.amount }}</td>
                <td style="padding: 5px;">{{ item.date_added }}</td>
                <td>
                    <form method="post">
                        {% csrf_token %}
                        <div style="display: flex; flex-direction: column;">
                            <button type="submit" name="increment" value="{{ item.id }}">
                                + Amount
                            </button>
                            <button type="submit" name="decrement" value="{{ item.id }}">
                                - Amount
                            </button>
                            <button type="submit" name="delete" value="{{ item.id }}">
                                Delete
                            </button>
                        </div>
                    </form>
                </td>
            </tr>
        {% endfor %}
     </table>
     ```
     
# Tugas 3


## **No 1**
1. Apa Perbedaan antara form `POST` dan `GET` dalam Django?
* `POST`
  - Fungsi utama dari form `POST` adalah untuk mengirimkan data ke server. `POST` biasanya digunakan untuk membuat,            meng-_update_ data, atau penghapusan data. Contohya seperti membuat file dan mengirimkan formulir.
* `GET`
  - Fungsi utama dari `GET` adalah untuk melakukan _request_ terhadap server untuk meminta data tanpa mengubah isi data.       `GET` biasanya digunakan untuk pencarian atau menampilkan data. Contohnya seperti mengambil data untuk ditampilkan di      halaman web seperti menampilkan artikel.
* Lainnya
  - Berikut merupakan perbedaan lainnya:
    | Perbedaan               | POST                             | GET                             |
    |-------------------------|------------------------------------------|---------------------------------| 
    | Batas _Character_          | Tidak ada batasan  | Panjang URL 2047 _character_ |
    | Keamanan                | Lebih aman (Karena data tidak terlihat dalam URL) | Kurang aman (Karena data terlihat dalam URL serta dapat dilihat oleh pihak ketiga) |
    | HTTP Status Code        | Jika POST _request_ berhasil, maka kodenya adalah status HTTP 201 | Jika GET _request_ berhasil, maka kodenya adalah kode status HTTP 200 (OK) |
    | _Input_ Data            |  Dilakukan melalui form |  dilakukan melalui link |
    | Pemanggilan Method      | POST menggunakan $_POST | GET menggunakan $_GET |


## **No 2**
2. Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?
* Extensible Markup Language (XML) biasanya digunakan untuk pertukaran data dengan server. XML memiliki jenis     
  struktur data berbasis _tag_ `<>`. Berikut adalah contoh dari kode XML:
     ```
        <?xml version="1.0" encoding="utf-8"?>
        <django-objects version="1.0">
            <object model="main.item" pk="2">
                <field name="name" type="CharField">Toyota Raize GR Sport</field>
                <field name="amount" type="IntegerField">1</field>
                <field name="price" type="IntegerField">50000</field>
                <field name="category" type="CharField">Compact</field>
                <field name="description" type="TextField">Raize Keluaran terbaru</field>
                <field name="date_added" type="DateField">2023-09-17</field>
            </object>
        </django-objects>
     ```

* JavaScript Object Notation (JSON) biasanya juga digunakan untuk pertukaran data dengan server. JSON memiliki struktur      data yang berbasis pasangan `key:value`. JSON cenderung memiliki _syntax _kode yang lebih ringkas dan mudah dibaca,        sehingga biasa digunakan untuk pertukaran data terstruktur antara server dengna _client web_. Berikut adalah               contoh dari kode JSON:
     ```
        [
            {
                "model": "main.item",
                "pk": 2,
                "fields": {
                    "name": "Toyota Raize GR Sport",
                    "amount": 1,
                    "price": 50000,
                    "category": "Compact",
                    "description": "Raize Keluaran terbaru",
                    "date_added": "2023-09-17"
                }
            }
        ]
     ```

* Hypertext Markup Language (HTML) tidak digunakan untuk pertukaran data, melainkan biasanya digunakan untuk mengatur        bagaimana data seperti _text, dan _image_, ditampilkan dalam suatu web. Berikut contoh kode HTML:
     ```
        <h1>CarRel's Shop</h1>
        <h5>Name: </h5>
        <p>{{ name }}<p>
        <h5>App Name: </h5>
        <p>{{ app_name }}<p>
        <h5>Class: </h5>
        <p>{{ class }}<p>
     ```
     


## **No 3**
3. Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
* JSON sering digunakan dalam pertukaran data antara aplikasi web modern karena memiliki format dan syntax yang         
  cenderung lebih singkat dan mudah dibaca.Hal tersebut dapat mempermudah _developer_ memahami struktur data teresbut.
* JSON kompatibel dengan javascript sehingga lebih terintegerasi pada banyak web.
* JSON lebih efisien dalam ukuran penyimpanan data.
  

## **No 4**
4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
* A. Membuat input form untuk menambahkan objek model pada app sebelumnya
    - Saya membuat input form yang bernama`forms.py` pada direktori aplikasi main. dengan isi sebagai berikut:
      ```
      from django.forms import ModelForm
      from main.models import Item
      
      class ItemForm(ModelForm):
          class Meta:
              model = Item
              fields = ["name","categories","description", "price", "amount"]
      ```
      Disini saya membuat class bernama ItemForm. Dalamnya berisi class Meta yang berisi model yang kita gunakan. Selain         itu berisi fields yang bisa diisi user, yaitu "name","categories","description", "price", "amount".

    - Setelah itu, saya membuat fungsi `create_item` pada `views.py` dengan isi sebagai berikut:
      ```
      def create_item(request):
      form = ItemForm(request.POST or None)
  
      if form.is_valid() and request.method == "POST":
          form.save()
          return HttpResponseRedirect(reverse('main:show_main'))
  
      context = {'form': form}
      return render(request, "create_item.html", context)
      ```
      Disini fungsi menerima sebuah parameter request. Dalam fungsi `create_item` saya membuat sebuah `ItemForm` dengan   
      argumen `request.POST` yang berbentuk QueryDict. Setelah itu divalidasi menggunakan `form.is_valid()` dan disimpan         dengan `form.save()`. Ketika berhasil disimpan, akan me-_return_ `HttpResponseRedirect(reverse('main:show_main'))`         untuk melakukan redirect setelah data form berhasil disimpan.

    - Setelah itu, saya mengubah dan menambahkan fungsi `show_main` pada `views.py` dengan kode sebagai berikut:
      ```
      def show_main(request):
        items = Item.objects.all()
        total_items = items.count()
        context = {
            'name': 'Muhammad Farrel Altaf',
            'class': "PBP B",
            'items': items,
            'item_count': total_items
        }
    
        return render(request, "main.html", context)
      ```
      disini saya menambahkan `item = Item.objects.all()` untuk menampilkan data item yang ditambahkan dan menambahkan     
      kode `total_items = item.count()` (SOAL BONUS) untuk mendapatkan jumlah item yang sudah ditambahkan dan dimasukan ke       context.

    - Setelah itu, saya meng-_import_ fungsi `create_item` di `urls.py` yang berada pada direkori aplikasi main
    
    - Setelah itu saya melakukan routing di `urls.py` pada direktori aplikasi main dengan menambahkan `path('create-item',       create_item, name='create_item')` di urlpatterns
    
    - Setelah itu saya membuat file `create_item.html` pada `templates` direktori aplikasi `main` dengan isi sebagai       
      berikut
      ```
      {% extends 'base.html' %} 

      {% block content %}
      <h1>Add New Item</h1>
      
      <form method="POST">
          {% csrf_token %}
          <table>
              {{ form.as_table }}
              <tr>
                  <td></td>
                  <td>
                      <input type="submit" value="Add Item"/>
                  </td>
              </tr>
          </table>
      </form>
      
      {% endblock %}
      ```
      Saya menggunakan `<form method="POST">` untuk mendefinisikan tipe form POST dan {% csrf_token %} untuk security.

    - Setelah itu saya mengubah dan menambahkan isi file `main.html` pada direktori `templates` seperti kode berikut
      ```
      {% extends 'base.html' %}

      {% block content %}
          <h1>CarRel's Shop</h1>
          <h5>Name: </h5>
          <p>{{ name }}</p>
          <h5>Class: </h5>
          <p>{{ class }}</p>
      
          <h5>Total Item: </h5>
          <p>Anda menyimpan {{ item_count }} jenis mobil pada aplikasi CarRel</p>
      
          <h5>Detail Item: </h5>
          <table border="1">
              <tr>
                  <th>Name</th>
                  <th>Categories</th>
                  <th>Description</th>
                  <th>Price</th>
                  <th>Amount</th>
                  <th>Date Added</th>
              </tr>
      
              {% comment %} Berikut cara memperlihatkan data produk di bawah baris ini {% endcomment %}
      
              {% for item in items %}
                  <tr>
                      <td>{{ item.name }}</td>
                      <td>{{ item.categories }}</td>
                      <td>{{ item.description }}</td>
                      <td>{{ item.price }}</td>
                      <td>{{ item.amount }}</td>
                      <td>{{ item.date_added }}</td>
                  </tr>
              {% endfor %}
          </table>
      
          <br />
      
          <a href="{% url 'main:create_item' %}">
              <button>
                  Add New Item
              </button>
          </a>
      {% endblock content %}

      ```
      Selain kode dari tutorial, saya menambahkan jumlah total item yang disimpan (BONUS) dan juga border untuk table.

      
* B. Tambahkan 5 fungsi views untuk melihat objek yang sudah ditambahkan dalam format HTML, XML, JSON, XML by ID, dan JSON      by ID.
    - HTML
      - Menampilkan main.html pada fungsi `show_main` di `views.py`
      ```
      def show_main(request):
        items = Item.objects.all()
        total_items = items.count()
        context = {
            'name': 'Muhammad Farrel Altaf',
            'class': "PBP B",
            'items': items,
            'item_count': total_items
        }
  
      return render(request, "main.html", context)
      ```

    - XML dan JSON
      - Meng-_import_
      ```
      from django.http import HttpResponse
      from django.core import serializers
      ```
      
      - Membuat fungsi show_xml di `views.py` dengan kode berikut:
      ```
      def show_xml(request):
      data = Item.objects.all()
      return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
      ```
      Serializerz disini digunakan untuk mentranslasikan objek model ke XML. Fungsi me-_return_ tampilan data dengan     
      format XML.
      
      - Membuat fungsi show_json di `views.py` dengan kode berikut:
      ```
      def show_json(request):
      data = Item.objects.all()
      return HttpResponse(serializers.serialize("json", data), content_type="application/json")

      ```
      Serializerz disini digunakan untuk mentranslasikan objek model ke JSON. Fungsi me-_return_ tampilan data dengan     
      format JSON.

    - XML by ID dan JSON by ID
      - Meng-_import_ (sama saja seperti diatas)
      ```
      from django.http import HttpResponse
      from django.core import serializers
      ```
      
      - Membuat fungsi show_xml_by_id di `views.py` dengan kode berikut:
      ```
      def show_xml_by_id(request, id):
      data = Item.objects.filter(pk=id)
      return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
      ```
      Serializerz disini digunakan untuk mentranslasikan objek model ke XML. Fungsi me-_return_ tampilan data dengan     
      format XML. Bedanya disini objek diambil berdasarkan ID.
      
      - Membuat fungsi show_xml_by_id di `views.py` dengan kode berikut:
      ```
      def show_json_by_id(request, id):
      data = Item.objects.filter(pk=id)
      return HttpResponse(serializers.serialize("json", data), content_type="application/json")
      ```
      Serializerz disini digunakan untuk mentranslasikan objek model ke JSON. Fungsi me-_return_ tampilan data dengan     
      format JSON. Bedanya disini objek diambil berdasarkan ID.
      
      
      
      
      




* C. Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2.
   - Pertama-tama saya melakukan _import_ pada `urls.py` dalam direktori `main`
   ```
   from django.urls import path
   from main.views import show_main, create_item, show_xml, show_json, show_xml_by_id, show_json_by_id
   ```
   - Lalu saya melakukan routing dengan kode:
    ```
    app_name = 'main'

    urlpatterns = [
        path('', show_main, name='show_main'),
        path('create-item', create_item, name='create_item'),
        path('xml/', show_xml, name='show_xml'),
        path('json/', show_json, name='show_json'),
        path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
        path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    ]
    
    ```
   - HTML sudah dilakukan sebelumnya dengan kode bagian:
     ```
     path('', show_main, name='show_main'),
     path('create-item', create_item, name='create_item'),
     ```
     Kita dapat mengaksesnya dengan menjalankan `http://localhost:8000`
     
   - XML dan JSON dengan kode bagian:
     ```
     path('xml/', show_xml, name='show_xml'),
     path('json/', show_json, name='show_json'),
     ```
     - Kita dapat mengaksesnya dengan menjalankan `http://localhost:8000/xml` untuk XML.
     - Kita dapat mengaksesnya dengan menjalankan `http://localhost:8000/json` untuk JSON.
     
   - XML by ID dan JSON by DD dengan kode bagian:
     ```
     path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
     path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
     ```
     - Kita dapat mengaksesnya dengan menjalankan `http://localhost:8000/xml](http://localhost:8000/xml/[ID]` untuk XML by ID.
     - Kita dapat mengaksesnya dengan menjalankan `http://localhost:8000/json](http://localhost:8000/json/[ID]` untuk JSON by ID.


## **No 5**
Mengakses kelima URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman.
* HTML
![Screenshot 2023-09-19 190031](https://github.com/LokSki22/CarRel/assets/119926379/ea69e0d5-7a79-443b-a269-f58855a4cd59)

* XML
![Screenshot 2023-09-19 190100](https://github.com/LokSki22/CarRel/assets/119926379/d509b078-908d-4f51-a1b2-63d90b63e8c5)

* JSON
![Screenshot 2023-09-19 190109](https://github.com/LokSki22/CarRel/assets/119926379/d5f8f45c-82a1-4bfd-9d5b-b04be8501b1d)

* XML by ID
![Screenshot 2023-09-19 190120](https://github.com/LokSki22/CarRel/assets/119926379/1363276b-576f-4198-9901-b8e7e3ac4a61)

* JSON by ID
![Screenshot 2023-09-19 190149](https://github.com/LokSki22/CarRel/assets/119926379/1f8eacc9-9ae2-4e32-a24f-db4b21181f9c)





# Tugas 2 


## **No 1**
1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
* A. Membuat sebuah proyek Django baru:
    - Saya membuat direktori lokal dengan bernama CarRel untuk menampung segala kebutuhan proyek saya.
    - Berikutnya, saya membuka command prompt, lalu membuat _virtual environment_ yang fungsinya untuk mengisolasi _package_ serta _dependencies_ dari aplikasi saya agar tidak bertabrakan dengan versi satu sama lain yang ada di _device_ yang saya pakai. Caranya adalah memasukan perintah di _command prompt_ sebagai berikut.
      ```
      python -m venv env
      ```
    - Berikutnya, untuk mengaktifkan _virtual environment_ saya memasukan perintah berikut:
      ```
      env\Scripts\activate.bat
      
    - Setelah mengaktifkan _virtual environment_ kita dapat menginstall semua dependencies yang diperlukan. Sebelumnya, saya membuat file bernama requirements.txt yang berisi _dependencies_ yang diperlukan seperti django, gunicorn, dan lain-lain.
    - Untuk menginstall _dependencies_ yang diperlukan, saya memasukan perintah berikut di _command prompt_:
    - ```
      pip install -r requirements.txt
      ```
    - Setelah menginstall _dependencies_, saya membuat proyek Django yang baru dengan memasukan perintah berikut:
    - ```
      django-admin startproject CarRel .
      ```
    - Karena proyek yang dibuat masih tahap uji coba, `ALLOWED HOST` pada `settings.py` saya tambahkan "*" agar setiap _hosts_ bisa mengakses aplikasi web
     ```
     ALLOWED_HOSTS = ["*"]
     ```
    - Setelah itu saya menambahkan file `.gitignore` karena ada _file-file_ yang tidak perlu git lacak.

* B. Membuat aplikasi dengan nama `main` pada proyek tersebut:
    - Kembali ke _command prompt_, saya menulis perintah berikut untuk membuat aplikasi 'main' pada proyek saya:
      ```
       python manage.py startapp main
      ```
    - Setelah menjalankan perintah diatas, akan terbentuk direktori bernama "main" yang berisi struktur awal aplikasi saya.
    - Setelah itu, saya membuka file `settings.py` di dalam direktori CarRel.
    - Setelah itu, saya menambahkan direktori baru `templates`pada direktori main dan menambahkan file `main.html` yang berfungsi mengatur tampilan aplikasi main pada web.

* C. Melakukan _routing_ pada proyek agar dapat menjalankan aplikasi `main`.
    - Untuk mengonfigurasi routing aplikasi dalam proyek saya, saya membuka file `urls.py` pada direktori proyek `libshop`. kemudian saya mengimpor fungsi `include` dari `django.urls` dan menambahkan  `path('main/',include('main.urls'))`yang berfungsi path untuk menuju tampilan main pada variabel `urlpattern`

* D. Membuat model pada aplikasi `main` dengan nama `Item` dan memiliki atribut wajib sebagai berikut. name sebagai nama item dengan tipe CharField. amount sebagai jumlah item dengan tipe IntegerField. description sebagai deskripsi item dengan tipe TextField.
    - Saya menambahkan atribut-atribut yang diperlukan yaitu sebagai berikut:
      - name 
      - amount 
      - price 
      - description 
      - date_added 
      - categories
        
* E. Membuat sebuah fungsi pada `views.py` untuk dikembalikan ke dalam sebuah _template_ HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
    - Saya menambahkan fungsi `show_main` dan berisi _context_ yang didalamnya berisi _name_ , _app_name_ , dan _class_
    - Isinya seperti bberikut:
    - ```
      def show_main(request):
            context = {
            'name': 'Muhammad Farrel Altaf',
            'app_name': 'CarRel',
            'class': "PBP B"
            }
      ```
    - Pada file '`main.html`, saya dapat mengakses isi dari _context_ dengan contohnya menulis `{{name}}`. `{{name}}` akan mengambil isi `name` dari _context_ yaitu 'Muhammad Farrel Altaf'

* F. Membuat sebuah _routing_ pada `urls.py` aplikasi main untuk memetakan fungsi yang telah dibuat pada `views.py`.
    - Saya mengimpor `path` dari `django.urls` dan impor `show_main` dari `main.views`
    - Setelah itu, saya membuat variable app_name yang berisi main seperti potongan kode berikut
    - ```app_name = 'main'```
    - Lalu menambahkan list bernama `urlpatterns` dan isi sebagai berikut
    -  ```
       urlpatterns = path('', show_main, name='show_main')

* G. Melakukan _deployment_ ke Adaptable terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
    - Saya membuat repositori baru bernama CarRel di github, lalu saya hubungkan direktori CarRel di lokal ke repositori CarRel di Github. Setelah itu, saya lakukan _add, commit, push_. Kemudian saya lakukan deploy di adaptable (Tidak lupa untuk memilih _template_ deployment, tipe basis data, versi _python_, masukan command yang sesuai, nama aplikasi yang sesuai dan centang bagian HTTP Listener on PORT).


## **No 2**
2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
<img width="2022" alt="Flow Django" src="https://github.com/LokSki22/CarRel/assets/119926379/68d2c5be-2f5f-48ea-b7d1-30802aaf66d5">

## **No 3**
3. Jelaskan mengapa kita menggunakan _virtual environment_? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
* Kita sangat disarankan untuk menggunakan _Virtual environment_ saat membuat suatu proyek Django. _Virtual environment_ dapat mengisolasi _package_ dan _dependency_ dari aplikasi sehingga tidak bertabrakan dengan versi lain yang ada di _device_ kita. _Virtual environment_ diperlukan karena jika kita memiliki banyak proyek, masing-masing proyek tidak akan berhubungan satu sama lain. Misal kita memiliki proyek A dan B yang sama-sama menggunakan Django 4.0, lalu kita menggunakan _virtual environment_ untuk meng-_update_ Django di proyek A menjadi Django 4.1, maka di proyek B Django tidak akan ikut ter-_update_ ke versi 4.1 karena proyek A dan B sudah saling terisolasi.
* Kita bisa saja membuat proyek Django tanpa menggunakan _virtual environment_, namun sangat tidak disarankan karena dapat memicu konflik antar proyek Django. Misal kita memiliki proyek A dan B yang menggunakan Django 4.0, lalu kita ingin meng-_update_ Django pada proyek A ke Django 4.1, maka Django pada proyek B akan ikut ter-_update_ ke versi 4.1. _Virtual environment_ sangat berguna untuk menghindari konflik antar proyek.


## **No 4**
4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
* MVC, MVT, dan MVVM ketiganya merupakan pola desain dan arstiektur perangkat lunak untuk mengembangkan aplikasi atau web.
* MVC
    - MVC merupakan singkatan dari _Model-View-Controller_.
    - _Model_ berperan dalam mengatur logika dan data dari aplikasi atau web serta mengubungkan aplikasi atau web dengan _database_ (_Backend_).
    - _View_ berperan menampilkan data dari _Model_ yang akan dilihat pengguna (_Front-End_).
    - _Controller_ berperan mengatur hubungan antara model dan view, dimana controller memproses aktivitas dari pengguna lalu berinteraksi dengan _Model_ dan mengubah _View_ (_Middle_). 
* MVT
    - MVT merupakan singkatan dari _Model-View-Template_.
    - _Model_ berperan dalam mengatur logika dan data dari aplikasi atau web serta mengubungkan aplikasi atau web dengan _database_ (_Backend_).
    - _View_ disini berperan seperti _Controller_ pada MVC untuk mengambil data dari _Model_ dan menghubungkannya dengan _Template_ (_Middle_).
    - _Template_ berperan untuk sisi menampilkan _user interface_ bagi pengguna (_Front-End_).
* MVVM
    - MVVM merupakan singkatan dari _Model-View-ViewModel_.
    - _Model_ berperan dalam mengatur logika dan data dari aplikasi atau web serta mengubungkan aplikasi atau web dengan _database_ (_Backend_).
    - _View_ berperan untuk menampilkan data dari _Model_ (_Front-End_).
    - _ViewModel_ berperan untuk mengubah data dari model ke dalam format yang lebih mudah untuk dibaca oleh _View_, selain itu ViewModel juga berguna untuk _data binding_ yaitu menyinkornkan penyajian data dan fungsi ke View serta pembaruan _Model_ (_Middle_).
* MVC dan MVT merupakan memiliki kemiripan dalam, perbedaanya hanya pada istilah komponen yang digunakan dan implementasi khusus pada _framework_nya masing-masing. Sedangkan MVVM memiliki perbedaan dari MVC dan MVT, dengan menekankan konsep _data binding_ yang tidak dipakai MVC dan MVT.


## **Bonus**
* Saya telah menambahkan tes baru yaitu merupakan tes model. Tes model berfungsi untuk mengecek apakah model yang dibuat sudah berkerja dengan baik atau tidak.


