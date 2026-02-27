// Validation against 02 Economic Tables & Projections REV7 (VDR 02.04)

const HOURS = 8760;
const RATE = 3000;
const DEPR_PER_CNC = 10000000 / 8; // 1,250,000
const SHOP_DEPR = 8600000 / 8; // 1,075,000
const FACILITY = 5200000;
const OPEX_PER_CNC = 150000;
const INTEREST = 0.075;
const OPS_SALARY = 1100000;
const ADMIN_SALARY = 1400000;
const ADMIN_FTE = 4;
const SHOP_DEBT = 4300000;

const STAFF_TABLE = [
    { cnc: 5, fte: 6 },
    { cnc: 10, fte: 10 },
    { cnc: 15, fte: 13 },
    { cnc: 20, fte: 16 },
    { cnc: 25, fte: 20 }
];

function getOpsFTE(cnc) {
    if (cnc <= 5) return 6;
    if (cnc >= 25) return 20;
    for (let i = 0; i < STAFF_TABLE.length - 1; i++) {
        const a = STAFF_TABLE[i], b = STAFF_TABLE[i + 1];
        if (cnc >= a.cnc && cnc <= b.cnc) {
            const ratio = (cnc - a.cnc) / (b.cnc - a.cnc);
            return a.fte + ratio * (b.fte - a.fte);
        }
    }
    return 20;
}

function getTotalDebt(cnc) {
    return Math.min(cnc, 5) * 5000000 + Math.max(0, cnc - 5) * 7000000 + SHOP_DEBT;
}

function calculate(cnc, utilPct, varPct) {
    const util = utilPct / 100;
    const varRate = varPct / 100;
    const revenue = cnc * HOURS * util * RATE;
    const opsFTE = getOpsFTE(cnc);
    const personnelOps = opsFTE * OPS_SALARY;
    const personnelAdmin = ADMIN_FTE * ADMIN_SALARY;
    const totalPersonnel = personnelOps + personnelAdmin;
    const deprCNC = cnc * DEPR_PER_CNC;
    const deprShop = SHOP_DEPR;
    const totalDebt = getTotalDebt(cnc);
    const financeCost = totalDebt * INTEREST;
    const facility = FACILITY;
    const otherOpex = cnc * OPEX_PER_CNC;
    const totalFixed = totalPersonnel + deprCNC + deprShop + financeCost + facility + otherOpex;
    const variableCosts = revenue * varRate;
    const totalCosts = totalFixed + variableCosts;
    const grossProfit = revenue - totalCosts;
    
    let customerShare = 0;
    if (util > 0.45) {
        const revenueAtThreshold = cnc * HOURS * 0.45 * RATE;
        const revenueAbove = revenue - revenueAtThreshold;
        const profitAbove = revenueAbove * (1 - varRate);
        customerShare = profitAbove * 0.50;
    }
    const aurelianProfit = grossProfit - customerShare;
    const breakEvenUtil = totalFixed / (cnc * HOURS * RATE * (1 - varRate)) * 100;
    
    return { revenue, totalCosts, grossProfit, customerShare, aurelianProfit, breakEvenUtil, totalFixed, variableCosts, totalPersonnel, deprCNC, deprShop, financeCost, otherOpex };
}

// CHECKPOINT 1: 20 CNC, 60%, 8% var -> Revenue ~315 MNOK, Cost ~92.75 MNOK, EBIT ~222.3 MNOK
console.log('\n=== CHECKPOINT 1: 20 CNC, 60%, 8% ===');
let r = calculate(20, 60, 8);
console.log('Revenue:', (r.revenue / 1e6).toFixed(1), 'MNOK (expected: ~315)');
console.log('Total Cost:', (r.totalCosts / 1e6).toFixed(2), 'MNOK (expected: ~92.75)');
console.log('  Personnel:', (r.totalPersonnel / 1e6).toFixed(1));
console.log('  Depr CNC:', (r.deprCNC / 1e6).toFixed(1));
console.log('  Depr Shop:', (r.deprShop / 1e6).toFixed(2));
console.log('  Finance:', (r.financeCost / 1e6).toFixed(2));
console.log('  Facility:', 5.2);
console.log('  Other Opex:', (r.otherOpex / 1e6).toFixed(1));
console.log('  Variable:', (r.variableCosts / 1e6).toFixed(1));
console.log('Gross Profit:', (r.grossProfit / 1e6).toFixed(1), 'MNOK');
console.log('Customer Share:', (r.customerShare / 1e6).toFixed(1), 'MNOK');
console.log('Aurelian Profit:', (r.aurelianProfit / 1e6).toFixed(1), 'MNOK (expected: ~222.3 before sharing, ~181 after)');

// CHECKPOINT 2: 5 CNC, 24%, 13% -> approximately break-even
console.log('\n=== CHECKPOINT 2: 5 CNC, 24%, 13% ===');
r = calculate(5, 24, 13);
console.log('Revenue:', (r.revenue / 1e6).toFixed(1), 'MNOK');
console.log('Total Cost:', (r.totalCosts / 1e6).toFixed(1), 'MNOK');
console.log('Profit:', (r.aurelianProfit / 1e6).toFixed(2), 'MNOK (expected: ~0)');
console.log('Break-even util:', r.breakEvenUtil.toFixed(1), '% (expected: ~24%)');

// Also check the 5-CNC break-even
r = calculate(5, 10, 13);
console.log('Break-even at 5 CNC, 13% var:', r.breakEvenUtil.toFixed(1), '%');

// CHECKPOINT 3: 20 CNC, 15%, 8% -> Revenue ~78.8 MNOK, EBIT ~5.0 MNOK
console.log('\n=== CHECKPOINT 3: 20 CNC, 15%, 8% ===');
r = calculate(20, 15, 8);
console.log('Revenue:', (r.revenue / 1e6).toFixed(1), 'MNOK (expected: ~78.8)');
console.log('Profit:', (r.aurelianProfit / 1e6).toFixed(1), 'MNOK (expected: ~5.0)');

// CHECKPOINT 4: 20 CNC, 65%, 8% -> Revenue ~341.6 MNOK, EBIT ~246.8 MNOK
console.log('\n=== CHECKPOINT 4: 20 CNC, 65%, 8% ===');
r = calculate(20, 65, 8);
console.log('Revenue:', (r.revenue / 1e6).toFixed(1), 'MNOK (expected: ~341.6)');
console.log('Gross Profit:', (r.grossProfit / 1e6).toFixed(1), 'MNOK');
console.log('Customer Share:', (r.customerShare / 1e6).toFixed(1), 'MNOK');
console.log('Aurelian Profit:', (r.aurelianProfit / 1e6).toFixed(1), 'MNOK (expected: ~246.8 from sensitivity table, before sharing)');
console.log('Break-even:', r.breakEvenUtil.toFixed(1), '%');
