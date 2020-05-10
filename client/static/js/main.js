$(document).ready(function () {
    const cats = document.getElementsByClassName("dish-category");
    const shops0 = document.getElementsByClassName("shops")[0];
    const shops = document.getElementsByClassName("shops");
    const dishCard = document.getElementsByClassName("dish-card");

    const accountIconNotClicked = document.getElementById("accountNotClicked");
    const accountIconClicked = document.getElementById("accountClicked");
    const orderBlock = document.getElementById("orderBlock");
    const accountBlock = document.getElementById("accountBlock");
    const mainPage = document.getElementById("main-page");
    const logoSmall = document.getElementById("logoSmall");
    const logoBig = document.getElementById("logoBig");
    const btnAdd = document.getElementById("btnAdd");
    const btnAddToCart = document.getElementById("btnAddToCart");
    const myOrderContent = document.getElementById("my-order-content");
    const emptyOrderText = document.getElementById("empty-order-text");
    const submitOrder = document.getElementById("submitOrder");
    const orderPriceValue = document.getElementById("order-price-value");
    const addToCart = document.getElementsByClassName("add-to-cart");
    // const headerNavChildren = document.getElementById("headerNav").children;
    let totalSum = 0;

    for (const a of addToCart) {

        a.addEventListener('click', function (event) {
            emptyOrderText.style.display = "none";
            const dishIdAndPrice = $(this).attr('id');
            const words = dishIdAndPrice.split('+');
            const dishId = words[0];
            const dishPrice = words[1];
            let dishPriceInt = parseInt(dishPrice);

            totalSum += dishPriceInt;
            orderPriceValue.innerHTML = "" + totalSum;

            var div = document.createElement("div");
            div.innerHTML = "" + dishId;
            div.className = "dishInOrder";

            var divPr = document.createElement("div");
            divPr.className = "dishInOrderPr";
            var spanPr = document.createElement("span");
            spanPr.innerHTML = dishPrice;
            spanPr.className = "dishInOrderPrSpan";
            divPr.appendChild(spanPr);

            var divParent = document.createElement("div");
            divParent.className = "dishInOrderFlexbox";

            var count = document.createElement("div");
            count.className = "dishInOrderCount";
            var span = document.createElement("span");
            span.innerHTML = "- 1 +";
            span.className = "dishInOrderSpan";
            count.appendChild(span);

            divParent.appendChild(div);
            divParent.appendChild(divPr);
            divParent.appendChild(count);

            myOrderContent.appendChild(divParent);
            if (submitOrder.style.backgroundColor !== "#503E9D") {
                submitOrder.style.backgroundColor = "#503E9D";
                submitOrder.style.color = "#FFFFFF";
            }

        })
    }


    if (accountBlock !== null) {
        accountBlock.style.display = "none";
        $('#btnAdd').hide();
        $('input').keyup(function () {
            if ($.trim(this.value).length > 0)
                $('#btnAdd').show()
            else
                $('#btnAdd').hide()
        });
        $('#btnAdd2').hide();
        $('input').keyup(function () {
            if ($.trim(this.value).length > 0)
                $('#btnAdd2').show()
            else
                $('#btnAdd2').hide()
        });
    }

    for (let i = 0; i < shops.length; i++) {
        shops[i].style.display = "none";
    }

    // TODO

    for (const dc of dishCard) {

        dc.addEventListener('click', function (event) {
            if (dc.style.backgroundColor === "#503E9D") {
                dc.style.backgroundColor = "#FFFFFF";
            } else {
                const shopId = $(this).attr('id');
                var shop = $('#' + shopId);
                shop.addClass("active-card");
                // console.log( $(this).getElementsByTagName("input"));

                // const formAddToCart = document.getElementById("formAddToCart");

                // var formAdd = $('#' + formAddToCart);

                // formAddToCart.children[0].value = $(this).attr('id');
                // console.log(formAddToCart.children[0].value);

                // $(this).querySelector("input").value = shopId;
                // document.getElementById("inputAddId").value = shopId;

                // console.log(document.getElementById(shopId));

                // shopId.addClass("active-card");

                // dc.style.backgroundColor = "#503E9D";
            }
        })
    }

    for (const button of cats) {
        button.addEventListener('click', function (event) {
            // TODO
            shops0.style.display = "none";
            console.log(document.getElementById($(this).attr('id') + "Shops"));
            document.getElementById($(this).attr('id') + "Shops").style.display = "flex";
        })
    }
    accountIconNotClicked.onclick = function () {
        accountIconNotClicked.style.display = "none";
        accountIconClicked.style.display = "flex";
        orderBlock.style.display = "none";
        accountBlock.style.display = "block";
    }
    // function openAccount() {
    //     accountIconNotClicked.style.display = "none";
    //     accountIconClicked.style.display = "flex";
    //     orderBlock.style.display = "none";
    //     accountBlock.style.display = "block";
    // }
    accountIconClicked.onclick = function () {
        accountIconClicked.style.display = "none";
        accountIconNotClicked.style.display = "flex";
        accountBlock.style.display = "none";
        orderBlock.style.display = "flex";
    }
    // function closeAccount() {
    //     accountIconClicked.style.display = "none";
    //     accountIconNotClicked.style.display = "flex";
    //     accountBlock.style.display = "none";
    //     orderBlock.style.display = "flex";
    // }

    // function openShopPage() {
    //     mainPage.style.display = "none";
    //     logoBig.style.display = "none";
    //     logoSmall.style.display = "block";
    //
    //     for (var i = 0, child; child = headerNavChildren[i]; i++) {
    //         child.style.alignSelf = "center";
    //     }
    // }

});