# Parameter Documentation

## Safety & Failsafe Parameters

### `FENCE_ACTION: 0`
- **Description**: Defines the vehicle's response when a geofence is breached.
- **Options**:
  - `0` = Report only (no action, just logs/notifications)
  - `1` = RTL (Return-to-Launch) or Land
  - `2` = Land (Copter) / Hold (Rover)
  - `3` = SmartRTL + RTL/Land (fallback)

### `BATT_LOW_VOLT: 0`
- **Description**: Voltage threshold (in volts) to trigger a low battery failsafe. Set to `0` to disable.

### `BATT_LOW_MAH: 0`
- **Description**: Remaining battery capacity (in mAh) to trigger a low battery failsafe. Set to `0` to disable.

### `BATT_CRT_VOLT: 0`
- **Description**: Critical voltage threshold for a secondary failsafe action. Set to `0` to disable.

### `BATT_CRT_MAH: 0`
- **Description**: Critical capacity threshold (mAh) for a secondary failsafe action. Set to `0` to disable.

---

## Preflight Checks & Sensors

### `EK3_GPS_Check: 0`
- **Description**: Disables EKF3's GPS health checks during pre-arm if set to `0`.

### `compass_orient: 0`
- **Description**: Sets the physical orientation of the compass. `0` = default (ROTATION_NONE).

---

## Signal Loss & Throttle Failsafe

### `thr_failsafe: 1`
- **Description**: Enables throttle failsafe. Triggers RTL/Land when throttle PWM drops below `FS_THR_VALUE`.

### `fs_gcs_enabl: 0`
- **Description**: Disables GCS (ground station) failsafe when set to `0`.

---

## Takeoff & Crash Detection

### `tkoff_accel_cnt: 1`
- **Description**: Number of consecutive acceleration samples required to detect takeoff.

### `tkoff_thr_max: 100`
- **Description**: Maximum throttle percentage during automatic takeoff.

### `crash_detect: 0`
- **Description**: Disables crash detection.

---

## Hardware-Specific

### `brd_heat_targ: -1`
- **Description**: Disables board temperature failsafe.

### `fs_vibe_enable: `
- **Description**: Controls vibration-based failsafe.

---

## HERE2 GPS Configuration

### `GPS_TYPE: 9`
- **Description**: Selects HERE2 GPS module.

### `CAN_D1_PROTOCOL: 1`, `CAN_D2_PROTOCOL: 1`
- **Description**: Configures CAN bus for HERE2 communication.

---

For more details on HERE2 GPS configuration, refer to the [CubePilot documentation](https://docs.cubepilot.org/user-guides/here-2/here-2-can-mode-instruction).

TODO add part for here3 "https://docs.cubepilot.org/user-guides/here-3/here-3-manual"