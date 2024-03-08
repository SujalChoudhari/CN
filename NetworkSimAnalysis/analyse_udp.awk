BEGIN {
    # Initialize variables
    total_packets_sent21 = 0
    total_packets_received21 = 0
    total_packets_dropped21 = 0
    total_delay21 = 0
    
    start_time21 = 1000
    end_time21 = 0
    
    # Additional variables for question 1
    packet_type_count = 0
}

{
    event = $1
    time = $2
    node = $3
    to = $4
    type = $5
    size = $6
    packet_id = $12

    # Additional logic for question 1
    if (event == "+") {
        if (type == "cbr") {
            if (!(packet_id in packet_types)) {
                packet_types[packet_id] = type
                ind_packet_sizes[packet_id] = size
                packet_type_count++
            }
        }
    }

    # Additional logic for question 2
    if (size != "" && !(size in packet_sizes)) {
        packet_sizes[size] = 1
    }

    if (type == "cbr" ) {
        # for 2 -> 1 
        if (event == "+" && node == 0) {  
            packets_sent[packet_id] = time
            total_packets_sent21++
            if (time < start_time21) {
                start_time21 = time
            }
        } else if (event == "r" && to == 3) { 
            if (packet_id in packets_sent) {
                delay = time - packets_sent[packet_id]
                total_delay21 += delay
                total_packets_received21++
                delete packets_sent[packet_id]
            }
            if (time > end_time21) {
                end_time21 = time
            }
        } else if (event == "d") {
            total_packets_dropped21++
        }
    }
}

END {
    # Calculate average end-to-end delay
    avg_delay21 = (total_packets_received21 > 0) ? (total_delay21 / total_packets_received21) : 0

    # Calculate throughput
    simulation_duration21 = (end_time21 - start_time21)
    throughput21 = (simulation_duration21 > 0) ? (total_packets_received21 / simulation_duration21) : 0

    # Print results for question 1
    printf("Table for Question 1:\n")
    printf("|Sr. No|Type of Packet| Size |\n")
    printf("|------|--------------|------|\n")
    for (packet_id in packet_types) {
        if( i % 200 == 0) {
            printf("| %4d | %12s | %4d |\n", i, packet_types[packet_id],ind_packet_sizes[packet_id])
            printf("|  .   |      ...     |   .  |\n")
        }
        i++;          
    }
   

    # Print results for question 2
    printf("\n\nPacket Sizes:\n")
    for (size in packet_sizes) {
        printf("%s ", size)
    }

    # Print results for question 3
    printf("\n\nCount number of data packets(CBR) for both scenarios transmitted between source to destination:\n")
    printf("0->3 (UDP): %d\n", total_packets_received21)

    # Print results for question 4
    printf("\n\nPacket Delivery Ratio:\n")
    printf("0->3 (UDP): %.2f%%\n", (total_packets_received21 / total_packets_sent21) * 100)
}
