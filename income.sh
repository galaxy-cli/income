#!/bin/bash
###############
#             #
#  income.sh  #
#             #
###############

read -p "Calculate income? [Y/N] " calculate_income

if [[ $calculate_income =~ [yY] ]]; then

	read -p "Calculate yearly income? [Y/N] " yearly

	if [[ $yearly =~ [yY]  ]]; then
		read -p "$ per year? " year

		weekly=$(($year/12/4))
		monthly=$(($year/12))

		per_week=$(printf "\$%'d\n" "$weekly")
		per_month=$(printf "\$%'d\n" "$monthly")
		per_year=$(printf "\$%'d\n" "$year")

		declare -A income_total
		income_total=(
			[$per_week]="per week"
			[$per_month]="per month"
			[$per_year]="per year"
		)

		for key in "${!income_total[@]}"; do
			printf "\n$key ${income_total[$key]}"
		done

		printf "\n\n"
	fi


	read -p "Calculate monthly income? [Y/N] " monthly

	if [[  $monthly  =~ [yY] ]]; then
		read -p "$ per hour? $" hour
		read -p "Workweek? " workweek

		week=$(($hour*$workweek))
		month=$(($week*4))
		year=$(($month*12))

		per_week=$(printf "\$%'d\n" "$week")
		per_month=$(printf "\$%'d\n" "$month")
		per_year=$(printf "\$%'d\n" "$year")

		declare -A income_total
		income_total=(
			[$per_week]="per week"
			[$per_month]="per month"
			[$per_year]="per year"
		)

		for key in "${!income_total[@]}"; do
			printf "\n$key ${income_total[$key]}"
		done

		printf "\n\n"
	fi
fi

read -p "Calculate rent? [Y/N] " calculate_rent

if [[ $calculate_rent =~ [yY] ]]; then

	read -p "Rent per month? $" rent
	read -p "Income per month? $" income
	read -p "Number of roommates? " roomates

	roomates=$((roomates + 1))
	remains=$((income - (rent/roomates)))
	yearly=$(($remains*12))
	percent=$((((rent/roomates)*100)/income))

	remains_c=$(printf "%'d\n" "$remains")
	yearly_c=$(printf "%'d\n" "$yearly")

	printf "\n\$$remains_c after monthly rent payments"
	printf "\n\$$yearly_c after yearly rent payments\n"
	printf "\n$percent%% of income goes to rent\n\n"
fi

read -p "Calculate income brackets? [Y/N] " calculate_income_bracket

if [[ $calculate_income_bracket =~ [yY] ]]; then
        read -p "Middle class income bracket? $" mid

        work=$(($mid/2));
        lowmid=$(echo "scale=0; $mid/1.5" | bc)
        uppmid_raw=$(echo "scale=0; $mid*1.5" | bc)
        uppmid=$(printf "%.0f" "$uppmid_raw")
        upp=$(($mid*2))
        wel=$(($mid*3))

        work_c=$(printf "%'d\n" "$work")
        lowmid_c=$(printf "%'d\n" "$lowmid")
        mid_c=$(printf "%'d\n" "$mid")
        uppmid_c=$(printf "%'d\n" "$uppmid")
        upp_c=$(printf "%'d\n" "$upp")
        wel_c=$(printf "%'d\n" "$wel")

        printf "\n\$$work_c annually or less is working class"
        printf "\n\$$lowmid_c annually is lower middle class"
        printf "\n\$$mid_c annually is middle class"
        printf "\n\$$uppmid_c annually is upper middle class"
        printf "\n\$$upp_c annually is upper class"
        printf "\n$\$$wel_c annually or more is wealthy\n\n"
fi
