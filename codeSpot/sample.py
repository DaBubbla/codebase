# Random little carlot inventory management system

cars = []

add_stock = input("Add inventory? [y/n] ")

while add_stock =='y':
    # Get a car from user
    make = input("Make: ")
    model = input("Model: ")
    year = input("Year: ")
    miles = input("Miles: ")

    # Create a diction object and save it to the list
    car = { "Make": make, "Model": model, "Year": year, "Miles": miles }
    cars.append(car)

    # Ask user if we should keep it going
    add_stock = input("Add inventory? [y/n]")

print('')
print("Here is the current inventory: ")


# Different flavors of printout
for c in cars:
    print("Make: " + c['Make'])
    print("Model: " + c['Model'])
    print("Year: " + c['Year'])
    print("Miles: " + c['Miles'])
    print('')

for car in cars:
    print(car)


    @app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock --- TODO """
    if request.method == "GET":
        return render_template("buy.html")

    else:
        # Proper symbol?
        quote = lookup(request.form.get("symbol"))
        if not quote:
            return apology("Invalid symbol", 400)

      
       
        # Calculate price of requested shares
        total_price = per_share * shares

        if total_price > cash_remaining:
            return apology("Insufficient funds! :( ")


        # Updates history and portfolio
        db.execute("UPDATE users SET cash = cash - :price WHERE id = :user_id",\
        price = total_price, user_id=session["user_id"])

        db.execute("INSERT INTO portfolio (user_id, symbol, name, shares, per_share) VALUES(:user_id, :symbol, :name, :shares, :price)", \
                        user_id=session["user_id"], symbol=quote["symbol"], name=quote["name"], shares=int(request.form.get("shares")), price=per_share )

        flash("Ka-Ching! Bought")

        return redirect(url_for("index"))
